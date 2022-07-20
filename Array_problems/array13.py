'''
Print the occurrence of each number if present else “NOT PRESENT”

Sample Input :

1 1 1 2 2 2 3 8 9 7

1 2 3 0 5

Sample Output :
3 3 1 Not Present Not Present
'''


def find_occurance(lst, variable):
    temp = {}
    occurance = []
    for i in lst:
        if i in temp:
            temp[i] = temp[i] + 1
        else:
            temp[i] = 1
    for i in variable:
        if i in temp.keys():
            occurance.append(str(temp[i]))
        else:
            occurance.append('Not present')
    return ' '.join(occurance)
variable = [1, 2, 3, 0, 5]
lst = [1, 1, 1, 2, 2, 2, 3, 8, 9, 7]
print(find_occurance(lst, variable))
