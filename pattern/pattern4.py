'''
Sample Input :
5

Sample Output :
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''

row = 5
count = 0
for i in range(1, row + 1):
    for j in range(1, i):
        count = count + 1
        print(count, end=" ")
    count = count + 1
    print(count)

from pattern5 import numeric_pyramid

numeric_pyramid(7)

