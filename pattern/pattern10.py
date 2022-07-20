'''
Sample Input :
5

Sample Output :
    1
   232
  34543
 4567654
567898765
'''

row = 5
for i in range(row+1):
    for j in range(row+1-i):
        print(j, end="")
    for j in range(2, i, -1):
        print(j, end="")
    print()
