'''
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


def least_occurance(lst):
    temp = {}
    least_number = []
    result = []
    for i in lst:
        if i in temp:
            temp[i] = temp[i] + 1
        else:
            temp[i] = 1
    # for key, value in temp.items():
    #     least_number.append(value)
    least_number = temp.values()
    least_number = list(least_number)
    least_number.sort()
    least_number = least_number[0]
    for key, value in temp.items():
        if value == least_number:
            result.append(key)
    result.sort(reverse=True)
    return result
lst = [1, 6, 4, 56, 56, 56, 6, 4, 2]
print(least_occurance(lst))
