#!usr/bin/env python
#-*- coding: utf-8 -*-

import json
import requests

from config.config import Config
class Authentication(object):

    def __init__(self, uid, auth_code):
        self.uid = uid
        self.auth_code = auth_code
        self.authentication_url = "https://sb-autenticacao-api.original.com.br/OriginalConnect/AccessTokenController"

    # Mounts dictionary for Original OAuth2 
    def mountOAuth2Data(self):
        config = Config()
        oauth_data = {
            "uid": self.uid,
            "auth_code": self.auth_code,
            "developer_key": config.get("developer_key"),
            "secret_key": config.get("secret_key")
        }

        return oauth_data

    # Gets OAuth Token using
    def getOAuth2Token(self):
        data = json.dumps(self.mountOAuth2Data())
        ori_response = requests.post(self.authentication_url, data=data)
        response = ori_response.content
        
        return response