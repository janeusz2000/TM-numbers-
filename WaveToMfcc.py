""" This program will convert wave files to MFCC"""
import numpy as np
from python_speech_features import mfcc

class WaveToMfcc(object):

    def __init__(self, array, rate):
        self.wave_array_ = array
        self.rate_ = rate

    def create_mfcc(self):
        mfcc_array = self.wave_array_
        for row in range(0, len(self.wave_array_)):
            for index in range(0, len(self.wave_array_[0]) - 1):
                 mfcc_array[row][index] = mfcc(self.wave_array_[row][index], self.rate_, appendEnergy=False)
        output = []
        for i in range(0, 10):
            mfcc_i = mfcc_array[0, i]
            for row in range(1, len(mfcc_array)):
                mfcc_i = np.concatenate((mfcc_i, mfcc_array[row][i]), axis=0)
            output.append(mfcc_i)
        return output
