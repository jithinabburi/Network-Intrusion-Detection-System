import pandas as pd

train = pd.read_csv(
    "data/KDDTrain+.txt",
    header=None
)

test = pd.read_csv(
    "data/KDDTest+.txt",
    header=None
)

print("Train Shape:", train.shape)
print("Test Shape:", test.shape)

print("\nFirst 5 Rows:")
print(train.head())