import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

def main():
    data = pd.read_csv("rawi3k.csv", header=None)
    (row_count, column_count) = data.shape

    records = []
    for row in range(row_count):
        records.append([x for x in data.iloc[row].tolist() if((type(x) != float) and (x != float('NaN')))])
    print(records)

if __name__ == "__main__":
    main()

