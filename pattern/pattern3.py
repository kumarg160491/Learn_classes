'''
Sample Input :
3 5

Sample Output :
* * * * *
* * * * *
* * * * *
'''
row = 3
col = 5

for i in range(row):
    for j in range(col):
        print('*', end=" ")
    print()