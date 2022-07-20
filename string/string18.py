'''
Sample Input :
I am kohli fan

Sample Output :
I ma ilhok naf
'''

string = 'I am kohli fan'
string = list(string.split())
temp = []
for i in string:
    temp.append(''.join(reversed(i)))
print(' '.join(temp))