#!usr/bin/env python
#-*- coding: utf-8 -*-

import re
import requests

class Product(object):

    def __init__(self, object_link):
        self.url = object_link
        self.value = self.setProductValue()

    def setProductValue(self):
        response = requests.get(self.url)
        result = re.search(r'R\$ ([0-9]+\.?[0-9]+,[0-9]{2})', response.content)
        formatted_value = result.group(0)[2:].replace(".", "").replace(",", ".")

        return float(formatted_value)