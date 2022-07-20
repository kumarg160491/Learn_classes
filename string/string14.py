'''
Output Description:
Print 1 if they are panagram and 0 if they are not

Sample Input :
nitin intni

Sample Output :
1
'''
s1 = 'nitin'
s2 = 'intni'

if sorted(s1) == sorted(s2):
    print(1)
else:
    print(0)
