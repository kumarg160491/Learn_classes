import pandas as pd
import matplotlib.pyplot as plt

author = ['Jitender', 'Purnima', 'Arpit', 'Jyoti']
article = [210, 211, 114, 178]

frame = {'Author': pd.Series(author), 'Article': pd.Series(article)}

df = pd.DataFrame(frame)
print(df)
# plt.figure(figsize=(2, 3))
# print(plt.hist(x=df['Article'], bins=10, alpha=1.0, color='black'))
# plt.show()

Age = [23, 24, 25, 23]
df['Age'] = pd.Series(Age)
print('\n', df)
# df.plot.bar()
# plt.show()

Age = [23, 24, 25]
df['Age'] = pd.Series(Age)
print('\n', df)