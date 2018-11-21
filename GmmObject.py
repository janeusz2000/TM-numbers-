"""
this program is going to trainning data drom MFCC input
"""
import sklearn.mixture.gaussian_mixture

class GmmObject(object):

    # constructor

    def __init__(self, name, n_components, max_iter, mfcc_input):
        self.gmm_ = sklearn.mixture.gaussian_mixture.GaussianMixture(n_components=n_components,
                                                                     max_iter=max_iter, init_params='random',
                                                                     random_state=20)
        self.name_ = name
        self.untrained = True
        self.mfcc_ = mfcc_input
        print("Object: " + name + " was successfully created")

    # destructor

    def __del__(self):
        print("Object: " + self.name_ + " was successfully destroyed")

    # methods:

    def train_data(self):
        self.gmm_.fit(self.mfcc_)
        self.untrained = False
        print("Training sucessfull")
        print("number of iterations: " + str(self.gmm_.n_init))

    def recognize(self):
        if self.untrained:
            print("GMM object wasn't trained yet!")
            return False
        else:
            outputlog = self.gmm_.score(self.mfcc_)
            if outputlog > -15:
                print("Object was recognised")
                return True
            elif outputlog > -30 and outputlog <= -15:
                print("Object was barely recognised")
                return True
            else:
                print("Object wasnt recognised")
                return False



