"""" this is main commander of a program"""

import Commander
import external_evaluator

commander = Commander.Commander(path_folder="train", winlen=None)
commander.cross_test()
commander.write_to_csv('results.csv')
print("program ended")
