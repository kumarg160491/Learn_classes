import pandas as pd

data = {
    'name': ['a', 'b', 'c'],
    'age': [23, 24, None],
    'salary': [1000, 1200, 1500],
    'emp_id': [1, 2, 3]
}
df = pd.DataFrame(data)
print(df)
df['experience'] = [2, 3, 5]

# checking name a and it's salary
print('\n', df[(df['name'] == 'a') & (df['salary'] < 1200)])

# update age where it is Nan
avg = round((df['age'].sum() / 3), 1)
print('\n', avg)
df['age'] = df['age'].fillna(avg)
print(df)

print(df[df['age'] == 15.7])

# use loc
print(df.loc[[1, 2]])
