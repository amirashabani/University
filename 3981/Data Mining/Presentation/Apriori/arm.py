import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

def pretty_rule(rule):
    items = [x for x in rule[0]]
    first = ", ".join(list(rule[2][0][0]))
    second = ", ".join((rule[2][0][1]))
    sup = rule[1]
    conf = rule[2][0][2]
    lift = rule[2][0][3]
    print(f"{first} => {second} (s: {sup:.3f}, c: {conf:.3f}, l: {lift:.3f})")

def main(file_path, attributes):
    # find index of attribute if it exists
    s_index = (attributes.index('-s') + 1) if('-s' in attributes) else -1
    c_index = (attributes.index('-c') + 1) if('-c' in attributes) else -1
    l_index = (attributes.index('-l') + 1) if('-l' in attributes) else -1

    # find attribute if index isn't -1
    min_s = float(attributes[s_index]) if s_index != -1 else 0.0025
    min_c = float(attributes[c_index]) if c_index != -1 else 0.5
    min_l = float(attributes[l_index]) if l_index != -1 else 3

    data = pd.read_csv("rawi3k.csv", header=None)
    (row_count, column_count) = data.shape

    records = []
    for row in range(row_count):
        records.append([x for x in data.iloc[row].tolist() if((type(x) != float) and (x != float('NaN')))])

    association_rules = list(apriori(records, min_support=min_s, min_confidence=min_c, min_lift=min_l, min_length=2))

    for rule in association_rules:
        pretty_rule(rule)

if __name__ == "__main__":
    if(len(sys.argv) >= 2):
        main(sys.argv[1], sys.argv[2:])
        sys.exit(0)
    else:
        print("No input file was specified.")
        sys.exit(1)

