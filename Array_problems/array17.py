'''


You are given an array of numbers. Print the least occurring element. If there is more than 1
element print all of them in decreasing order of their value.

Input Description:
You are given a number ‘n’ denoting size of array. Next line contains n space separated numbers.

Output Description:
Print the number as mentioned

Sample Input :
9
1 6 4 56 56 56 6 4 2

Sample Output :
2 1


'''
lst = [1, 6, 4, 56, 56, 56, 6, 4, 2]
temp1 = []
temp2 = []
temp = {}
for i in lst:
    if i in temp:
        temp[i] = temp[i] + 1
    else:
        temp[i] = 1
# for key, value in temp.items():
#     temp1.append(value)
temp1 = list(temp.values())
temp1.sort()
least_value = min(temp1)
for key, value in temp.items():
    if value == least_value:
        temp2.append(key)
temp2.sort(reverse=True)
print(temp2)