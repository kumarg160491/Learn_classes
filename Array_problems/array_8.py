'''
Given a number N, print the odd digits in the number(space seperated) or print -1 if there is no odd digit in the given number.
Input Size : N <= 100000
Sample Testcase :
INPUT
2143
OUTPUT
1 3

Algorithm:
lst=[2,1,4,3]
temp = []
for i in lst:
    if i%2!=0:
    temp.append(i)
else temp.append(-1)
'''
lst = [2, 1, 4, 3]
temp = []
for i in lst:
    if i % 2 != 0:
        temp.append(i)
if not temp:
    print(-1)
else:
    print(temp)
