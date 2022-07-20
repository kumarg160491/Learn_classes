'''
Given a string 'S' and a character 'K', find how many times 'K' got repeated in 'S'.If 'K' is not found in 'S' print -1
Input Size : |s| <= 100000
Sample Testcase :
INPUT
codekata a
OUTPUT
2
'''


def find_value(key):
    sample_input = 'codekata'
    sample_input = list(sample_input)
    temp = {}
    for i in sample_input:
        if i in temp:
            temp[i] = temp[i] + 1
        else:
            temp[i] = 1

    print(temp[key])


find_value('a')
