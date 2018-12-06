"""" this is main commander of a program"""

import Commander
import external_evaluator

commander = Commander.Commander(path_folder="train", winlen=0.015)
commander.eval_test()
commander.write_to_csv_else('result.csv')

print("program ended")
