import pandas as pd

data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
    'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'E': ['E1', 'E2', 'E3', 'E4', 'E5']}
df = pd.DataFrame(data)
print(df)

# df = df.drop(['A'], axis=1)
# print(df)

# print(df.drop(df.columns[[0, 1]], axis=1, inplace=True))

print(df.drop(df.loc[:, ['A', 'B']].columns, axis=1))