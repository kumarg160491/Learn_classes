import pandas as pd

df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
                   'points': [5, 7, 7, 9, 12, 9, 9, 4],
                   'assists': [11, 8, 10, 6, 6, 5, 9, 12]},
                  index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
print(df)

print(df.loc[['E'], ['team']])

print(df.loc['E':, :'assists'])

print('\n', df.iloc[4:6])
print('\n', df.iloc[4:, :])
