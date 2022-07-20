'''
Sample Input :
3 5

Sample Output :
* * * * *
*       *
* * * * *
'''
row = 3
columns = 5
for i in range(row):
    if i == 0 or i == (row - 1):
        for j in range(columns):
            print('*', end=" ")
    else:
        for j in range(columns):
            if j == 0 or j == columns-1:
                print('*', end=" ")
            else:
                print(' ',end = " ")

    print()
