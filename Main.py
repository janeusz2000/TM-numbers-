""" this is main commander of a program"""

import GmmObject
import WaveReader
import WaveToMfcc

reader = WaveReader.WaveReader("train")
(signals, rate) = reader.read_all()
converter = WaveToMfcc.WaveToMfcc(signals, rate)
mfcc_array = converter.create_mfcc()

table = []
for each in range(0, 9):
    table.append(GmmObject.GmmObject(16, mfcc_array[each]))

for each in table:
    each.train_data()

print("YAY")

