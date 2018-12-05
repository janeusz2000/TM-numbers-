import numpy as np


class Classificator(object):
    def __init__(self, mfcc_input, gmm_list_input):
        self.mfcc_ = mfcc_input
        self.gmm_list = gmm_list_input
        self.n_correct = 0
        self.n_iterations = 0

    # methods:
    def classify(self, mfcc_digit):
        self.n_iterations += 1
        scores_list = []
        for gmm in self.gmm_list:
            gmm = gmm.gmm_.score(self.mfcc_)
            scores_list.append(gmm)
        max_likelihood = np.max(scores_list)
        if scores_list.index(max_likelihood) == mfcc_digit:
            self.n_correct += 1
        return scores_list.index(max_likelihood)

    def classify_norm(self, mfcc_digit):
        self.n_iterations += 1
        scores_list = []
        for gmm in self.gmm_list:
            gmm = gmm.gmm_.score(self.mfcc_)
            scores_list.append(gmm)
        mean_list = []
        for i in range(0, 10):
            list_without_x = np.delete(scores_list, i)
            mean_list.append(np.mean(list_without_x))
        scores_list = np.array(scores_list) - np.array(mean_list)
        max_likelihood = np.max(scores_list)

        if np.argwhere(scores_list == max_likelihood) == mfcc_digit:
            self.n_correct += 1
        return np.argwhere(scores_list == max_likelihood)

    def get_RR(self):
        return self.n_correct/self.n_iterations






