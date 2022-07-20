'''
Sample Input :
5

Sample Output :
*  *  *  *  *
*  *  *  *
*  *  *
*  *
*
'''

row = 5

for i in range(row+1):
    for j in range(row-i):
        print("*", end=" ")
    print()