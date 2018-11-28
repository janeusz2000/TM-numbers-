import GmmObject
import WaveReader
import WaveToMfcc
import Classificator

class Commander(object):

    def __init__(self, path_folder):
        self.reader_ = WaveReader.WaveReader(path_folder)
        (self.signals, self.rate) = self.reader_.read_all()
        self.converter = WaveToMfcc.WaveToMfcc(self.signals, self.rate)
        self.mfcc_array_ = self.converter.glue()
        self.gmm_table_ = []

    def train_all(self):
        self.gmm_table_ = []
        for each in range(0, 9):
            self.gmm_table_.append(GmmObject.GmmObject(16, self.mfcc_array_[each]))
        for each in self.gmm_table_:
            each.train_data()
