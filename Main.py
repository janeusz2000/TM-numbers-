""" this is main commander of a program"""

import Commander

commander = Commander.Commander(path_folder="train", winlen=None )
commander.cross_test()
commander.write_to_csv('results_LL_Norm.csv')
print("program ended")