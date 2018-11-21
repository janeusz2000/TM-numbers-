"""
this program is going to trainning data drom MFCC input
"""
import sklearn.mixture.gaussian_mixture

class GmmObject(object):

    # constructor

    def __init__(self, n_components, n_init_in, mfcc_input):
        self.gmm_ = sklearn.mixture.gaussian_mixture.GaussianMixture(n_components=n_components,
                                                                     max_iter=2000, init_params='random',
                                                                     random_state=20, n_init=n_init_in)
        self.untrained = True
        self.mfcc_ = mfcc_input

    # methods:

    def train_data(self):
        self.gmm_.fit(self.mfcc_)
        self.untrained = False
        print("Training successful")
        print("number of iterations: " + str(self.gmm_.n_iter_))

    def recognize(self, mfcc_input):
        if self.untrained:
            print("GMM object wasn't trained yet!")
            return -99999
        else:
            outputlog = self.gmm_.score(mfcc_input)
            if outputlog > -15:
                print("Object was recognised")
                return outputlog
            elif outputlog > -30 and outputlog <= -15:
                print("Object was barely recognised")
                return outputlog
            else:
                print("Object wasnt recognised")
                return outputlog



