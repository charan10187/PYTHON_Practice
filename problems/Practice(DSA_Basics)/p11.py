# Problem 11 -- Fibonacci Series
n=int(input("N = "))

a=0
b=1
if n==0:
    print(a)
elif n==1:
    print(a)
else:
    print(a)
    print(b)
    for fib in range(0,n-2):
        fib=a+b
        a=b
        b=fib
        print(fib)

n=10        
def fib(n):
    num=[0,1]
    for i in range(2,n-1):
        sum=num[i+2]+num[i-1]
        num.append(sum)
        # num[i]=sum
        
    print(num)