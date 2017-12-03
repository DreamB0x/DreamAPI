#!usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from flask import request
from flask.ext.cors import CORS, cross_origin

from account.account import Account
from product.product import Product
from auth.auth import Authentication

app = Flask( __name__ )
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

token = "Bearer MzVjNTdhMTAtZDc5Ni0xMWU3LWJjNTEtMDA1MDU2OWE3MzA1OmV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUowZVhCbElqb2lUMEYxZEdnaUxDSnBZWFFpT2pFMU1USXlOREkxT1Rjc0ltVjRjQ0k2TVRVeE1qWTNORFU1Tnl3aVlYVmtJam9pTldJMFpqZG1PR1lpTENKcGMzTWlPaUphZFhBdWJXVWdSMkYwWlhkaGVTSXNJbk4xWWlJNklqTTFZelUzWVRFd0xXUTNPVFl0TVRGbE55MWlZelV4TFRBd05UQTFOamxoTnpNd05TSXNJbXAwYVNJNklqTm1ZVFkxTUdVd0xXUTNPVFl0TVRGbE55MWhOMk13TFdNeE56WXlaRFl3TlRRME5pSjkuUmEzTGY2VmtEM3QwdG9wRFoxSHBwRWt2OTVzNUVWRjRDU2hSdTNUcEFHTQ=="

############################################
#               GET TOKEN
############################################
@app.route("/oauth2/get/token", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def authenticate():
    uid = request.args["uid"]
    auth_code = request.args["auth_code"]
    token = Authentication(uid, auth_code)

    return token.getOAuth2Token()

############################################
#               USER BALANCE
############################################
@app.route("/user/balance", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def getBalance():
    # token = request.form["ori_token"]
    customer = Account(token)

    return customer.getBalance()

############################################
#               USER CLASSIFY
############################################
@app.route("/user/classify", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def classifyUser():
    # token = request.form["ori_token"]
    customer = Account(token)

    return jsonify({
        "customer.category": customer.predictUserType()
    })

############################################
#           USER REWARDS BALANCE
############################################
@app.route("/user/balance/rewards", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def rewardBalance():
    # token = request.form["ori_token"]
    customer = Account(token)

    return jsonify({
        "reward.balance": customer.getRewardBalance()
    })

############################################
#           USER CAN BUY PRODUCT
############################################
@app.route("/user/canbuyproduct", methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def canBuy():
    # token = request.form["ori_token"]
    product_url = request.form["product_url"]
    customer, product = Account(token), Product(product_url)

    if customer.canBuyUsingDebit(product):
        status = 202
        message = "user can buy this product"
    else:
        status = 203
        message = "user cannot buy this product"

    return jsonify({
        "buy.status": status,
        "buy.message": message
    })

if __name__ == '__main__':
    app.run()