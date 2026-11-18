def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(i,"fact is",fact)
fact(5)