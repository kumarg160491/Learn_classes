s = '1331'
s = list(s)
temp = []
for i in s:
    temp.append(int(i))


temp1 = []
for i in range(1, len(temp)-1):
    print(i)
    if temp[i]!= temp[i+1] and temp[i]!= temp[i-1] :
        temp1.append(temp[i])
    print('--')
print(temp1)