#!usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np
from sklearn.naive_bayes import GaussianNB

class NaiveBayes(object):

    def __init__(self, transactions):
        self.transactions = transactions

    def values_array(self):
        features_list = []
        label_list = []

        for transaction in self.transactions:
            transaction_value = float(transaction["transaction_amount"])
            
            if transaction_value <= 300:
                label = "nutella"
            elif transaction_value > 300 and transaction_value <= 600:
                label = "medio"
            else:
                label = "raíz"

            features_list.append([transaction_value, 1000])
            label_list.append(label)

        return (features_list, label_list)

    def classify(self):
        features, labels = self.values_array()
        model = GaussianNB()
        model.fit(features, labels)
        classification = model.predict([[520.00, 1000.00]])

        return classification[0]