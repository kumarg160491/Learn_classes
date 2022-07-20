'''
You are given with a list of size ‘n’. The list is imposed with a condition that all
elements must be of range 0 to n-1.
Your task is to rearrange the numbers such that arr[i] becomes arr[arr[i]].

Input Description:
You are given size of array ‘n’.n space separated numbers in next line.

Output Description:
Print all elements after rearranging.

Sample Input :
5
4 0 2 1 3

Sample Output :
3 4 2 0 1
'''

lst = [4, 0, 2, 1, 3]
a = []
for i in range(0, len(lst)):
    a.append(lst[lst[i]])
print(a)