#!usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np
from sklearn.naive_bayes import GaussianNB

class Predictioner(object):

    def __init__(self, transactions):
        self.transactions = transactions

    def values_array(self):
        features_list = []
        label_list = []

        for transaction in self.transactions:
            transaction_value = float(transaction["transaction_amount"])
            
            if transaction_value <= 300:
                label = "baixo"
            elif transaction_value > 300 and transaction_value <= 600:
                label = "medio"
            else:
                label = "hardcore"

            features_list.append([transaction_value, 1000])
            label_list.append(label)

        return (features_list, label_list)

    def Model(self):
        features, labels = self.values_array()
        model = GaussianNB()
        model.fit(features, labels)

        print model.predict([[520.00, 1000.00]])

if __name__ == "__main__":
    model = Predictioner()
    model.Model()