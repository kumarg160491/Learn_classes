'''
Sample Input :
5

Sample Output :
12345
4321
123
21
1
'''


def print_variable(i, j):
    if j > i:
        for k in range(i, j + 1):
            print(k, end=" ")
    else:
        for k in range(i, j-1, -1):
            print(k, end=" ")


def reverse_pyramid(n):
    row = col = n
    odd = 0
    for i in range(1, n):
        if n <= 0:
            break
        print_variable(1, n)
        print()
        if n-1 <= 0:
            break
        print_variable(n - 1, 1)
        print()
        n = n - 2


print(reverse_pyramid(6))
