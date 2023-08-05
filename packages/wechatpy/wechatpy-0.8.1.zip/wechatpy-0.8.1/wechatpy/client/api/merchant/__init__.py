# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from wechatpy.client.api.base import BaseWeChatAPI

from .category import MerchantCategory
from .stock import MerchantStock
from .express import MerchantExpress
from .group import MerchantGroup
from .shelf import MerchantShelf
from .order import MerchantOrder
from .common import MerchantCommon


class WeChatMerchant(BaseWeChatAPI):

    def __init__(self, *args, **kwargs):
        super(WeChatMerchant, self).__init__(*args, **kwargs)

        # sub APIs
        self.category = MerchantCategory(self._client)
        self.stock = MerchantStock(self._client)
        self.express = MerchantExpress(self._client)
        self.group = MerchantGroup(self._client)
        self.shelf = MerchantShelf(self._client)
        self.order = MerchantOrder(self._client)
        self.common = MerchantCommon(self._client)

    def create(self, product_data):
        return self._post(
            'merchant/create',
            data=product_data
        )

    def delete(self, product_id):
        return self._post(
            'merchant/del',
            data={
                'product_id': product_id
            }
        )

    def update(self, product_id, product_data):
        product_data['product_id'] = product_id
        return self._post(
            'merchant/update',
            data=product_data
        )

    def get(self, product_id):
        return self._post(
            'merchant/get',
            data={
                'product_id': product_id
            }
        )

    def get_by_status(self, status):
        return self._post(
            'merchant/getbystatus',
            data={
                'status': status
            }
        )

    def update_product_status(self, product_id, status):
        return self._post(
            'merchant/modproductstatus',
            data={
                'product_id': product_id,
                'status': status
            }
        )
