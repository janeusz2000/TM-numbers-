""" this program is going to wirte results to csv"""

import csv

class ResultsCsv(object):

    # constructor

    def __init__(self, results):
        self.results_ = results
        self.writer = csv.writer("Results.csv")


    # methods

    def write_to_csv(self):
        print("writing to CSV")

