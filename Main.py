""" this is main commander of a program"""

import GmmObject
import WaveReader
import WaveToMfcc

reader = WaveReader.WaveReader("train")
reader.read_all()


converter = WaveToMfcc.WaveToMfcc(reader)
gmm = GmmObject