'''
you are given with array of numbers.you have to find whether array is beautiful or not. A beautiful array is an array whose sum of all numbers is divisible by 2, 3 and 5

Input Description:
You are given a number ‘n’ denoting the size of array.Next line contains n space separated numbers.

Output Description:
Print 1 if array is beautiful and 0 if it is not

Sample Input :
5
5 25 35 -5 30

Sample Output :
1

'''
total = 0
lst = [5, 25, 35, -5, 30]
for i in lst:
     total = total + i
print(total)
if total%2 ==0 and total%3 == 0 and total%5==0:
    print(1)
else:
    print(0)
