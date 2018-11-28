import numpy as np


class Classificator(object):
    def __init__(self, mfcc_input, gmm_list_input):
        self.mfcc_ = mfcc_input
        self.gmm_list = gmm_list_input

    # methods:
    def classify(self, mfcc_digit):
        scores_list = []
        for gmm in self.gmm_list:
            gmm = gmm.gmm_.score(self.mfcc_)
            scores_list.append(gmm)
        max_likelihood = np.max(scores_list)
        return scores_list.index(max_likelihood)




