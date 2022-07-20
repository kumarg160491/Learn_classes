'''
INPUT
string 2
OUTPUT
sTrInG
'''

sample_input = 'string'
sample_input = list(sample_input)
temp = []
for i in range(0, len(sample_input)):
    if i % 2==0:
        temp.append(sample_input[i])
    else:
        temp.append(sample_input[i].upper())
print(''.join(temp))