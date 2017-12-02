#!usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from flask import request
from flask.ext.cors import CORS, cross_origin

from account.account import Account
from auth.auth import Authentication

app = Flask( __name__ )
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def welcome():
    return "Welcome to dreambox"

@app.route("/getToken", methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def authenticate():
    uid = request.form["uid"]
    auth_code = request.form["auth_code"]
    token = Authentication(uid, auth_code)

    return token.getOAuth2Token()

@app.route("/getBalance", methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def getBalance():
    # token = request.form["ori_token"]
    token = "Bearer MzVjNTdhMTAtZDc5Ni0xMWU3LWJjNTEtMDA1MDU2OWE3MzA1OmV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUowZVhCbElqb2lUMEYxZEdnaUxDSnBZWFFpT2pFMU1USXlOREkxT1Rjc0ltVjRjQ0k2TVRVeE1qWTNORFU1Tnl3aVlYVmtJam9pTldJMFpqZG1PR1lpTENKcGMzTWlPaUphZFhBdWJXVWdSMkYwWlhkaGVTSXNJbk4xWWlJNklqTTFZelUzWVRFd0xXUTNPVFl0TVRGbE55MWlZelV4TFRBd05UQTFOamxoTnpNd05TSXNJbXAwYVNJNklqTm1ZVFkxTUdVd0xXUTNPVFl0TVRGbE55MWhOMk13TFdNeE56WXlaRFl3TlRRME5pSjkuUmEzTGY2VmtEM3QwdG9wRFoxSHBwRWt2OTVzNUVWRjRDU2hSdTNUcEFHTQ=="
    customer = Account(token)

    return customer.getBalance()

if __name__ == '__main__':
    app.run()