import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

def pretty_rule(rule):
    print(rule)

def main(file_path):
    data = pd.read_csv("rawi3k.csv", header=None)
    (row_count, column_count) = data.shape

    records = []
    for row in range(row_count):
        records.append([x for x in data.iloc[row].tolist() if((type(x) != float) and (x != float('NaN')))])

    association_rules = list(apriori(records, min_support=0.0025, min_confidence=0.5, min_lift=3, min_length=2))

    for rule in association_rules:
        pretty_rule(rule)

if __name__ == "__main__":
    if(len(sys.argv) >= 2):
        main(sys.argv[1])
        sys.exit(0)
    else:
        print("No input file was specified.")
        sys.exit(1)

