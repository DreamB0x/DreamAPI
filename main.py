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

@app.route("/teste", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def teste():
    uid = "08a3d180-d787-11e7-bc51-0050569a7305"
    auth_code = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiT0F1dGhBdXRoQ29kZSIsImlhdCI6MTUxMjIzNjM1OSwiZXhwIjoxNTEyMjM2OTU5LCJhdWQiOiI1YjRmN2Y4ZiIsImlzcyI6Ilp1cC5tZSBHYXRld2F5Iiwic3ViIjoiYjlhODQ5MjAtZDc4Ny0xMWU3LWJjNTEtMDA1MDU2OWE3MzA1IiwianRpIjoiYjlkMGRmYzEtZDc4Ny0xMWU3LWJjNTEtNzE0ZDBjZjQyMDFjIn0.TaobR5_Mee4Jxj_AMA12T0Zz6VzGyXRkoev_J3oo_JU"
    token = Authentication(uid, auth_code)
    return jsonify(token.getOAuth2Token())

if __name__ == '__main__':
    app.run()