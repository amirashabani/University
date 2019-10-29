import pandas as pd

# read train data from csv file in Data folder
train = pd.read_csv('Data/en_train.csv')

# number of (rows, columns) of train dataframe
print(train.shape)

# a sample of 5 rows from train dataframe
print(train.head())

# read test data from csv file in Data folder
test = pd.read_csv('Data/en_test.csv')

# number of (rows, columns) of test dataframe
print(test.shape)

# a sample of 5 rows from test dataframe
print(test.head())

# display rows which have a 'sentence_id' of 44 (from train dataframe)
print(train[train['sentence_id'] == 44])
