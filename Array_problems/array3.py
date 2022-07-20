'''
You  are given n numbers and window size ‘w’

Your task is to print the first index which has 0

Input Description:
You are given two numbers ‘n’ and ‘w’ n representing size of array and ‘w’ size of window

Output Description:
Print the index of first 0(1 basedindexing),if there is no index with 0 print -1

Algorithm:
temp = []
n = [1, 0, 6, 7, 4, 0, 9]
w = 7
for i in n:
if i != 0 print temp.append(-1)
else temp.append(
'''

temp = []
n = [1, 0, 6, 7, 4, 0, 9]
for index in range(0, len(n)):
    if n[index] != 0:
        temp.append(-1)
    else:
        temp.append(index)
print(temp)
