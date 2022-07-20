'''
fib using recursion
fib normally
factorial
quadilateral roots
list [1,a,b,[c,4,[5,e,f],7],9] = [1,a,b,c,4,5,e,f,7,9]
'''


# fib using recursion
def fibonacci(x):
    if x <= 1:
        return x
    else:
        fib = fibonacci(x - 1) + fibonacci(x - 2)
        return fib


x = int(input("Enter number of terms:"))
for i in range(x):
    print(fibonacci(i), end=" ")
