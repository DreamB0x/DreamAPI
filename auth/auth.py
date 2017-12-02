#!usr/bin/env python
#-*- coding: utf-8 -*-

import json
import requests

class Authentication(object):

    def __init__(self, uid, auth_code):
        self.uid = uid
        self.auth_code = auth_code
        self.authentication_url = "https://sb-autenticacao-api.original.com.br/OriginalConnect/AccessTokenController"

    def mountOAuth2Data(self):
        oauth_data = {
            "uid": self.uid,
            "auth_code": self.auth_code,
            "developer_key": "28f955c90b3a2940134ff1a970050f569a87facf",
            "secret_key": "dd385cd0b59c013560400050569a7fac"
        }

        return oauth_data

    def getOAuth2Token(self):
        data = json.dumps(self.mountOAuth2Data())
        ori_response = requests.post(self.authentication_url, data=data)
        response = ori_response.content
        
        return response