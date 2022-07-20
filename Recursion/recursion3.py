"""
['a', ['b', ['c', ['d']], 'e'], 'f']
"""


def recur(x):
    temp = []
    for i in x:
        if type(i) == list:
            temp += recur(i)
        else:
            temp += i
    return temp


print(recur(['a', ['b', ['c', ['d']], 'e'], 'f']))

'''
addition in recursion
'''


def add_rec(x):
    if x == 1:
        return x
    else:
        x = x + add_rec(x - 1)
        return x


print(add_rec(10))
