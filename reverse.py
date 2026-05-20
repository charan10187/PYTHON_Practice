n=str(input())
dig=0
while n>0:
    rem=n%10
    dig=dig*10+rem
    n=n//10
print(dig)