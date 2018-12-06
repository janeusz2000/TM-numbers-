"""" this is main commander of a program"""

import Commander
import external_evaluator

commander = Commander.Commander(path_folder="train", winlen=0.015)
commander.cross_test()
commander.write_to_csv('result_cross.csv')
print("program ended")
