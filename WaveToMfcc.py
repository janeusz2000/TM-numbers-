""" This program will convert wave files to MFCC"""

from python_speech_features import mfcc

class WaveToMfcc(object):

    def __init__(self, array, rate):
        self.wave_array_ = array
        self.rate_ = rate

    def create_mfcc(self):
        mfcc_array = []
        for row in range(0, len(self.wave_array_)):
            for index in range(0, len(self.wave_array_[0])-1):
                mfcc_feat = mfcc(self.wave_array_[row][index], self.rate_, appendEnergy=False)
                mfcc_array.append(mfcc_feat)
                if index == 9:
                    mfcc_array.append(self.wave_array_[row][10])
        return mfcc_array
