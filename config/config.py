#!usr/bin/env python
#-*- coding: utf-8 -*-

import os
import json

class Config(object):

    def __init__(self):
        self.setUpConfig()

    # Setup config using config file
    def setUpConfig(self):
        file = open(os.getcwd() + "/config/config.json", "r")
        self.config_struct = json.loads(file.read())

    # Gets config value by key
    def get(self, config_key):
        return self.config_struct[config_key]