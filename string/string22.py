'''
Given a number N, print the sum of the squares of its digits.
Input Size : 1 <= N <= 1000000000000000000
Sample Testcase :
INPUT
19
OUTPUT
82
'''

sample_input = 19
sample_input = list(str(sample_input))
print(sample_input)
sum = 0
for i in sample_input:
    sum = sum + (int(i) * int(i))
print(sum)
