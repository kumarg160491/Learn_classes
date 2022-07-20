fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
value = list(map(lambda s: s[0] == "A", fruit))
print(value)

for value in value:
    print(value)

num = [1, 2, 3, 4, 5, 6]

print(list(map(lambda x: x % 2 == 0, num)))

from functools import reduce
import math

print(reduce(lambda x, y: x + y, num))

import pandas as pd

df = pd.DataFrame({'Team': ['A', 'B', 'C', 'D'],
                   'Points': [23, 45, 34, 45],
                   'assists': [11, 8, 10, 6]
                   }
                  )
print(df)
print(df.loc[[1, 2], ['Team', 'Points']])
print(df.iloc[2:]['Team'])
