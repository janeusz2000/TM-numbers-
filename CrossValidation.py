import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import LeavePOut
from sklearn.model_selection import TimeSeriesSplit


class CrossValidation(object):
    def __init__(self, mfcc_input, n_test):
        self.mfcc_ = mfcc_input
        self.n_test_ = n_test
        #self.X_train, self.X_test, self.y_train, self.y_test = \
            #train_test_split(self.mfcc_, 1, test_size=self.n_test_)
        x = self.mfcc_[:, 10].T
        kf = KFold(n_splits=11)
        lpo = LeavePOut(p=2)
        tscv = TimeSeriesSplit(n_splits=21)
        TimeSeriesSplit(max_train_size=21, n_splits=21)
        for train, test in kf.split(x, ):
            print("%s %s" % (train, test))
