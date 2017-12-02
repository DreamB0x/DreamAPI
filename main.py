#!usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from flask import request
from flask.ext.cors import CORS, cross_origin

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

if __name__ == '__main__':
    app.run()