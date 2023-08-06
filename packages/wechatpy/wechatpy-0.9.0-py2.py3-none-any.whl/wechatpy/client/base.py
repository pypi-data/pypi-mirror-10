# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import time
import copy

import requests

from wechatpy._compat import json
from wechatpy.exceptions import WeChatClientException, APILimitedException
from wechatpy.client.api.base import BaseWeChatAPI


class BaseWeChatClient(object):

    API_BASE_URL = ''

    def __new__(cls, *args, **kwargs):
        self = super(BaseWeChatClient, cls).__new__(cls)
        for name, api in self.__class__.__dict__.items():
            if isinstance(api, BaseWeChatAPI):
                api = copy.deepcopy(api)
                api._client = self
                setattr(self, name, api)
        return self

    def __init__(self, access_token=None):
        self._access_token = access_token
        self.expires_at = None

    def _request(self, method, url_or_endpoint, **kwargs):
        if not url_or_endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url', self.API_BASE_URL)
            url = '{base}{endpoint}'.format(
                base=api_base_url,
                endpoint=url_or_endpoint
            )
        else:
            url = url_or_endpoint

        # 群发消息上传视频接口地址 HTTPS 证书错误，暂时忽略证书验证
        if url.startswith('https://file.api.weixin.qq.com'):
            kwargs['verify'] = False

        if 'params' not in kwargs:
            kwargs['params'] = {}
        if isinstance(kwargs['params'], dict) and \
                'access_token' not in kwargs['params']:
            kwargs['params']['access_token'] = self.access_token
        if isinstance(kwargs.get('data', ''), dict):
            body = json.dumps(kwargs['data'], ensure_ascii=False)
            body = body.encode('utf-8')
            kwargs['data'] = body

        res = requests.request(
            method=method,
            url=url,
            **kwargs
        )
        res.raise_for_status()
        result = res.json()
        return self._handle_result(result, method, url, **kwargs)

    def _handle_result(self, result, method=None, url=None, **kwargs):
        if 'base_resp' in result:
            # Different response in device APIs. Fuck tencent!
            result = result['base_resp']
        if 'errcode' in result:
            result['errcode'] = int(result['errcode'])

        if 'errcode' in result and result['errcode'] != 0:
            errcode = result['errcode']
            errmsg = result['errmsg']
            if errcode == 42001:
                # access_token expired, fetch a new one and retry request
                self.fetch_access_token()
                kwargs['params']['access_token'] = self._access_token
                return self._request(
                    method=method,
                    url_or_endpoint=url,
                    **kwargs
                )
            elif errcode == 45009:
                # api freq out of limit
                raise APILimitedException(errcode, errmsg)
            else:
                raise WeChatClientException(errcode, errmsg)

        return result

    def get(self, url, **kwargs):
        return self._request(
            method='get',
            url_or_endpoint=url,
            **kwargs
        )

    _get = get

    def post(self, url, **kwargs):
        return self._request(
            method='post',
            url_or_endpoint=url,
            **kwargs
        )

    _post = post

    def _fetch_access_token(self, url, params):
        """ The real fetch access token """
        res = requests.get(
            url=url,
            params=params
        )
        result = res.json()
        if 'errcode' in result and result['errcode'] != 0:
            raise WeChatClientException(result['errcode'], result['errmsg'])

        self._access_token = result['access_token']
        expires_in = 7200
        if 'expires_in' in result:
            expires_in = result['expires_in']
        self.expires_at = int(time.time()) + expires_in
        return result

    def fetch_access_token(self):
        raise NotImplementedError()

    @property
    def access_token(self):
        """ WeChat access token """
        if self._access_token:
            if not self.expires_at:
                # user provided access_token, just return it
                return self._access_token

            timestamp = time.time()
            if self.expires_at - timestamp > 60:
                return self._access_token

        self.fetch_access_token()
        return self._access_token
