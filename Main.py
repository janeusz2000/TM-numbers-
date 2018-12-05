""" this is main commander of a program"""

import Commander

commander = Commander.Commander(path_folder="train", winlen=None, nfilt=None, ncep=None)
commander.cross_test()
commander.write_to_csv('results.csv')
print("program ended")