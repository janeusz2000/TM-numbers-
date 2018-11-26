import numpy as np
from sklearn.model_selection import cross_val_score


class CrossValidation(object):
    def __init__(self, mfcc_input, n_trail):
        self.mfcc_ = mfcc_input
        self.n_trail_ = n_trail
