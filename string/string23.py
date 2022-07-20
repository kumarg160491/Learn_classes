'''
Given a string S,count the maximum number of times a character repeated in the string.If no character is repeated print '0'.
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
codekata
OUTPUT
2
'''

sample_input = 'codekata'
sample_input = list(sample_input)
print(sample_input)
temp = {}

for i in sample_input:
    if i in temp:
        temp[i] = temp[i] + 1
    else:
        temp[i] = 1

print(max(list(temp.values())))