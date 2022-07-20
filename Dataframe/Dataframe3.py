import pandas as pd

data = {
    'Employee_name': ['a', 'b', 'c', 'd', 'e', 'f'],
    'Salary': [1000, 2000, 1500, 2000, 1500, 3000],
    'Post': ['Deputy Manager 1', 'Manager', 'Deputy Manager 2', 'Deputy Manager 1',
             'Manager', 'Regional Manager'],
    'Department': ['Sales', 'Insurance', 'Collection', 'Trade', 'Trade', 'Collection']
}

# Importing Employee details
Employee_dataframe = pd.DataFrame(data)
print(Employee_dataframe)

# Find which employee is having salary greater than 1500
Emp_salary_greater_than_1500 = Employee_dataframe[Employee_dataframe['Salary'] > 1500]
print('\n', Emp_salary_greater_than_1500)

# Find employee salary equals to 1500
Empl_salary_1500 = Employee_dataframe.loc[Employee_dataframe['Salary'] == 1500]
print('\n', Empl_salary_1500)

# Find Role as 'Regional Manager'
Emp_role_regional_manager = Employee_dataframe[Employee_dataframe['Post'] == 'Regional Manager']
print('\n', Emp_role_regional_manager)

# Find particular Manager index
Index_manager = Employee_dataframe.iloc[1:2]
print('\n', Index_manager)

# Selecting particular columns using indexing
print('\n', Employee_dataframe.iloc[:, [0,2,3]])

# Selecting where Post is Deputy Manager 1
Role_deputy_manager_1 = Employee_dataframe.iloc[list(Employee_dataframe['Post'] == 'Deputy Manager 1')]
print('\n', Role_deputy_manager_1)

# Indexing
print('\n', Employee_dataframe.iloc[1])

print('\n', Employee_dataframe.iloc[:, [0, 3, 2]])

print('\n', Employee_dataframe.iloc[list(Employee_dataframe['Salary'] >= 2000)])

print('\n', Employee_dataframe.iloc[list(Employee_dataframe['Department'] == 'Collection')])
