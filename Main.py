""" this is main commander of a program"""

import GmmObject
import WaveReader
import WaveToMfcc
import Classificator


reader = WaveReader.WaveReader("train")
(signals, rate) = reader.read_all()
converter = WaveToMfcc.WaveToMfcc(signals, rate)
mfcc_array = converter.create_mfcc()

gmm_table = []
for each in range(0, 9):
    gmm_table.append(GmmObject.GmmObject(16, mfcc_array[each]))

for each in gmm_table:
    each.train_data()

for i in range(0, len(mfcc_array)):
    classificator = Classificator.Classificator(mfcc_array[i], gmm_table)
    classification = classificator.classify()
    print(classification)

