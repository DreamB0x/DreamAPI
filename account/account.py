#!usr/bin/env python
#-*- coding: utf-8 -*-

import json
import requests
from NB.naivebayes import NaiveBayes

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
        response_dict = json.loads(response)
        response_dict["current_balance"] = float(response_dict["current_balance"]) 
        
        return response_dict 

    def getRewardBalance(self):
        ori_response = requests.get(self.base_url + "/rewards/v1/balance", headers=self.headers)
        response = json.loads(ori_response.content)["current_balance"]

        return float(response)

    # Checks if user can buy product
    def canBuyUsingDebit(self, product):
        balance = self.getBalance()["current_balance"]
        return  balance >= product.value

    # Gets history of transactions
    def getTransactions(self):
        response = requests.get(self.base_url + "/accounts/v1/transaction-history", headers=self.headers)
        transactions = json.loads(response.content)
        
        return transactions

    # Classifies user type
    def predictUserType(self):
        transactions = self.getTransactions()
        nbayes = NaiveBayes(transactions)

        return str(nbayes.classify())
