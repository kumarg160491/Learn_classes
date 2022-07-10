'''
Sample Input :
7
10 7 9 3 2 1 15

Sample Output :
7 3 3 2 1 -1 -1

'''

temp = []
x = [10, 7, 9, 3, 2, 1, 15]
for i in range(0, len(x)-1):
    for j in range(i+1, len(x)):
        if x[j] < x[i]:
            temp.append(x[j])
            break
    else:
        temp.append(-1)
temp.append(-1)
print(temp)
