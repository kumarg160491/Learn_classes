'''
Given a number N, print the odd digits in the number(space seperated) or print -1 if there is no odd digit in the given number.
Input Size : N <= 100000
Sample Testcase :
INPUT
2143
OUTPUT
1 3
'''
[2, 1, 4, 3]


# def odd_digit(lst):
#     temp = []
#     for i in lst:
#         if i % 2 != 0:
#             temp.append(i)
#         if not temp:
#             return -1
#     print(temp)
#
#
# lst = [1,2,3,4,5]
# print(odd_digit(lst))


def odd_digit(lst):
    return [i for i in lst if i % 2 != 0]


lst = [1, 2, 3, 4, 5]
print(odd_digit(lst))
