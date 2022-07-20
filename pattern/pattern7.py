'''
Sample Input :
5

Sample Output :
12345
1234
123
12
1
'''

row = col = 5

for i in range(row):
    for j in range(1, row+1-i):
        print(j, end="")
    print()
