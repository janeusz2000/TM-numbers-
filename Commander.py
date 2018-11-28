import GmmObject
import WaveReader
import WaveToMfcc
import Classificator
import CrossValidation
import numpy as np


class Commander(object):

    def __init__(self, path_folder):
        self.reader_ = WaveReader.WaveReader(path_folder)
        (self.signals, self.rate) = self.reader_.read_all()
        self.converter = WaveToMfcc.WaveToMfcc(self.signals, self.rate)
        self.mfcc_array_ = self.converter.glue_all()
        self.gmm_table_ = []
        self.cross_split = CrossValidation.CrossValidation(self.converter.list_of_speakers, 2)


    def train_all(self):
        self.gmm_table_ = []
        for each in range(0, 9):
            self.gmm_table_.append(GmmObject.GmmObject(16, self.mfcc_array_[each]))
        for each in self.gmm_table_:
            each.train_data()

    def train(self, mfcc):
        gmm_table_ = []
        for each in range(0, 9):
            gmm_table_.append(GmmObject.GmmObject(16, mfcc[each]))
        for each in gmm_table_:
            each.train_data()
        return gmm_table_

    def cross_test(self):
        results = []
        for train, test in self.cross_split.get_split():
            train_mfcc = self.converter.glue(train)
            trained_gmm = self.train(train_mfcc)
            classificator = Classificator.Classificator([], trained_gmm)
            results_onetest = np.zeros((20, 1))
            idx=0
            names = np.chararray((20, 1), itemsize=12, unicode=True)
            for one_test in test:
                mfcc_table = self.converter.glue(one_test)
                for i in range(0, 10):
                    classificator.mfcc_ = mfcc_table[i]
                    results_onetest[idx, 0] = classificator.classify(i)
                    names[idx, 0] = self.converter.list_of_speakers[one_test]+"" + str(i) + '_.wav'
                    idx +=1
            results_onetest = np.concatenate((results_onetest, names), axis=1)
            results.append(results_onetest)
        return results





