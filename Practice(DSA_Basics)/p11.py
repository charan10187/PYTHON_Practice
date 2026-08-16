# Problem 11 -- Fibonacci Series
n=int(input("N = "))

a=0
b=1
print(a)
print(b)
for fib in range(0,n-2):
    fib=a+b
    a=b
    b=fib
    print(fib)
    
