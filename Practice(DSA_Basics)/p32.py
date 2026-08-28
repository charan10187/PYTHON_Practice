'''
    Problem 32 -- Remove All Odd Digits
    Input : 123456
    Output : 246

'''

N=int(input("Input : "))
result=0
rev=0

while N!=0:
    digit = N%10
    if digit%2==0:
        result=result*10+digit
    N//=10

while result!=0:
    dig=result%10
    rev=rev*10+dig
    result//=10
print("output : ",rev)
