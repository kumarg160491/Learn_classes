'''


You are given a number with duplicate digits your task is to remove the immediate duplicate digits and print the result

Input Description:
You are given a long string of digits

Output Description:
Print the desired result print -1 if result length is 0

Sample Input :
1331

Sample Output :
11

Algorithm:

list = [1,3,3,1]
temp = []
for index in range(0 to len(list))
if index != index+1:
temp.append(lst[index])

'''
lst = [1, 3, 3, 1]
temp = []
for i in range(1, len(lst)):
    if lst[i] != lst[i - 1]:
        temp.append(i)
print(temp)



