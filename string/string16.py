string = 'HeLlo'
temp = ''
count1 = 0
count2 = 0
count3 = 0

for a in string:
    if (a.isupper()) == True:
        count1 += 1
        temp += (a.lower())
    elif (a.islower()):
        count2 += 1
        temp += (a.upper())
    elif (a.isspace()):
        count3 += 1
        temp += a

print(temp)
