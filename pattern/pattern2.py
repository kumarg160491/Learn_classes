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
n = 5

for i in range(n):
    for j in range(n-i):
        print(j+1, end=" ")
    print()