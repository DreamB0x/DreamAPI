#!usr/bin/env python
#-*- coding: utf-8 -*-

import json
import requests

from config.config import Config

class Account(object):

    def __init__(self, oauthToken):
        config = Config()
        self.base_url = "https://sandbox.original.com.br"
        self.headers = {
            "Authorization": oauthToken,
            "developer-key": config.get("developer_key")
        }

    # Gets user balance - (current, avaiable limit, current limit)
    def getBalance(self, version="v1"):
        ori_response = requests.get(self.base_url + "/accounts/v1/balance", headers=self.headers)
        response = ori_response.content

        return response

    def canBuyUsingDebit(self, product):
        print "produto: {}".format(product.value)
        return float(json.loads(self.getBalance())["current_limit"]) >= product.value
