#!usr/bin/env python
#-*- coding: utf-8 -*-

import json

class Config():

    def __init__(self):
        self.setUpConfig()

    # Setup config using config file
    def setUpConfig(self):
        file = open("/home/vinicius/Python/originalhack/config/config.json", "r")
        self.config_struct = json.loads(file.read())

    # Gets config value by key
    def get(self, config_key):
        return self.config_struct[config_key]