'''
Sample Input :
5

Sample Output :
1
22
333
4444
55555
'''


def numeric_pyramid(n):
    row = col = n
    print(__name__)
    for i in range(1, row + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()


# numeric_pyramid(7)

if __name__ == '__main__':
    print(__name__)
    numeric_pyramid(7)
