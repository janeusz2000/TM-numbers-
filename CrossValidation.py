import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import pandas as pd


class CrossValidation(object):
    def __init__(self, mfcc_input, n_test):
        self.mfcc_ = mfcc_input
        self.n_test_ = n_test
        df = pd.DataFrame(self.mfcc_.data)
        y = self.mfcc_.target
        self.X_train, self.X_test, self.y_train, self.y_test = \
            train_test_split(df, y, test_size=self.n_test_)
