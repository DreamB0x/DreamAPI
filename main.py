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

    return jsonify(customer.getBalance())

############################################
#               USER CLASSIFY
############################################
@app.route("/user/classify", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def classifyUser():
    # token = request.form["ori_token"]
    customer = Account(token)

    return jsonify({
        "customer_category": customer.predictUserType()
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
        "reward_balance": customer.getRewardBalance()
    })

############################################
#           USER CAN BUY PRODUCT
############################################
@app.route("/user/canbuyproduct", methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def canBuy():
    # token = request.form["ori_token"]
    product_url = request.form["product_url"]
    customer = Account(token)
    product = Product(product_url)

    return jsonify({
        "buy_status": customer.canBuyUsingDebit(product),
        "buy_classification": customer.predictUserType()
    })

############################################
#           PRODUCT INFO
############################################
@app.route("/product/info", methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def productInfo():
    product_url = request.form["product_url"]
    product = Product(product_url)
    plots = product.getMonthlyPlots()

    return jsonify({
        "product_value": product.value,
        "product_x": plots[0],
        "product_monthly": plots[1]
    })


############################################
#         INVESTMENTS SUMMARY
############################################
@app.route("/user/investments", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def investmentsSummary():
    customer = Account(token)
    return jsonify(customer.getInvestmentsSummary())


if __name__ == '__main__':
    app.run()