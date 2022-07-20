'''
Sample Input :
5

Sample Output :
*****
 ****
  ***
   **
    *
'''

row = 5

for i in range(row):
    print(" "*i,end="")
    for j in range(1, row+1 -i):
        print("*",end="")
    print()

