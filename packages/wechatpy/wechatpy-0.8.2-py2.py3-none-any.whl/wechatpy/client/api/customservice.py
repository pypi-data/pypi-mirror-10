# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import hashlib
import time
import datetime

from wechatpy.utils import to_binary, NotNoneDict
from wechatpy.client.api.base import BaseWeChatAPI


class WeChatCustomService(BaseWeChatAPI):

    def add_account(self, account, nickname, password):
        """
        添加客服账号
        详情请参考
        http://mp.weixin.qq.com/wiki/1/70a29afed17f56d537c833f89be979c9.html

        :param account: 完整客服账号，格式为：账号前缀@公众号微信号
        :param nickname: 客服昵称，最长6个汉字或12个英文字符
        :param password: 客服账号登录密码
        :return: 返回的 JSON 数据包
        """
        password = to_binary(password)
        password = hashlib.md5(password).hexdigest()
        return self._post(
            'customservice/kfaccount/add',
            data={
                'kf_account': account,
                'nickname': nickname,
                'password': password
            }
        )

    def update_account(self, account, nickname, password):
        """
        更新客服账号
        详情请参考
        http://mp.weixin.qq.com/wiki/1/70a29afed17f56d537c833f89be979c9.html

        :param account: 完整客服账号，格式为：账号前缀@公众号微信号
        :param nickname: 客服昵称，最长6个汉字或12个英文字符
        :param password: 客服账号登录密码
        :return: 返回的 JSON 数据包
        """
        password = to_binary(password)
        password = hashlib.md5(password).hexdigest()
        return self._post(
            'customservice/kfaccount/update',
            data={
                'kf_account': account,
                'nickname': nickname,
                'password': password
            }
        )

    def delete_account(self, account, nickname, password):
        """
        删除客服账号
        详情请参考
        http://mp.weixin.qq.com/wiki/1/70a29afed17f56d537c833f89be979c9.html

        :param account: 完整客服账号，格式为：账号前缀@公众号微信号
        :param nickname: 客服昵称，最长6个汉字或12个英文字符
        :param password: 客服账号登录密码
        :return: 返回的 JSON 数据包
        """
        password = to_binary(password)
        password = hashlib.md5(password).hexdigest()
        return self._post(
            'customservice/kfaccount/del',
            data={
                'kf_account': account,
                'nickname': nickname,
                'password': password
            }
        )

    def get_accounts(self):
        """
        获取客服账号列表
        详情请参考
        http://mp.weixin.qq.com/wiki/1/70a29afed17f56d537c833f89be979c9.html

        :return: 客服账号列表
        """
        res = self._get('customservice/getkflist')
        return res['kf_list']

    def upload_headimg(self, account, media_file):
        """
        上传客服账号头像
        详情请参考
        http://mp.weixin.qq.com/wiki/1/70a29afed17f56d537c833f89be979c9.html

        :param account: 完整客服账号
        :param media_file: 要上传的头像文件，一个 File-Object
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'customservice/kfaccount/uploadheadimg',
            params={
                'kf_account': account
            },
            files={
                'media': media_file
            }
        )

    def get_online_accounts(self):
        """
        获取在线客服接待信息
        详情请参考
        http://mp.weixin.qq.com/wiki/9/6fff6f191ef92c126b043ada035cc935.html

        :return: 客服接待信息列表
        """
        res = self._get('customservice/getonlinekflist')
        return res['kf_online_list']

    def create_session(self, openid, account, text=None):
        """
        多客服创建会话
        详情请参考
        http://mp.weixin.qq.com/wiki/2/6c20f3e323bdf5986cfcb33cbd3b829a.html

        :param openid: 客户 openid
        :param account: 完整客服账号
        :param text: 附加信息，可选
        :return: 返回的 JSON 数据包
        """
        data = NotNoneDict()
        data['openid'] = openid
        data['kf_account'] = account
        data['text'] = text
        return self._post(
            'customservice/kfsession/create',
            data=data
        )

    def close_session(self, openid, account, text=None):
        """
        多客服关闭会话
        详情请参考
        http://mp.weixin.qq.com/wiki/2/6c20f3e323bdf5986cfcb33cbd3b829a.html

        :param openid: 客户 openid
        :param account: 完整客服账号
        :param text: 附加信息，可选
        :return: 返回的 JSON 数据包
        """
        data = NotNoneDict()
        data['openid'] = openid
        data['kf_account'] = account
        data['text'] = text
        return self._post(
            'customservice/kfsession/close',
            data=data
        )

    def get_session(self, openid):
        """
        获取客户的会话状态
        详情请参考
        http://mp.weixin.qq.com/wiki/2/6c20f3e323bdf5986cfcb33cbd3b829a.html

        :param openid: 客户 openid
        :return: 返回的 JSON 数据包
        """
        return self._get(
            'customservice/kfsession/getsession',
            params={'openid': openid}
        )

    def get_session_list(self, account):
        """
        获取客服的会话列表
        详情请参考
        http://mp.weixin.qq.com/wiki/2/6c20f3e323bdf5986cfcb33cbd3b829a.html

        :param account: 完整客服账号
        :return: 客服的会话列表
        """
        res = self._get(
            'customservice/kfsession/getsessionlist',
            params={'kf_account': account}
        )
        return res['sessionlist']

    def get_wait_case(self):
        """
        获取未接入会话列表
        详情请参考
        http://mp.weixin.qq.com/wiki/2/6c20f3e323bdf5986cfcb33cbd3b829a.html

        :return: 返回的 JSON 数据包
        """
        return self._get('customservice/kfsession/getwaitcase')

    def get_records(self, start_time, end_time, page_index,
                    page_size=10, user_id=None):
        """
        获取客服聊天记录
        详情请参考
        http://mp.weixin.qq.com/wiki/19/7c129ec71ddfa60923ea9334557e8b23.html

        :param start_time: 查询开始时间，UNIX 时间戳
        :param end_time: 查询结束时间，UNIX 时间戳，每次查询不能跨日查询
        :param page_index: 查询第几页，从 1 开始
        :param page_size: 每页大小，每页最多拉取 1000 条
        :param user_id: 普通用户的标识，对当前公众号唯一

        :return: 返回的 JSON 数据包
        """
        if isinstance(start_time, datetime.datetime):
            start_time = time.mktime(start_time.timetuple())
        if isinstance(end_time, datetime.datetime):
            end_time = time.mktime(end_time.timetuple())
        record_data = {
            'starttime': int(start_time),
            'endtime': int(end_time),
            'pageindex': page_index,
            'pagesize': page_size
        }
        if user_id:
            record_data['openid'] = user_id
        res = self._post(
            'customservice/getrecord',
            data=record_data
        )
        return res['recordlist']
