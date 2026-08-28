'''
    Problem 31 -- Remove All Even Digits
    Input : 123456
    Output : 135

'''

N=int(input("Input : "))
odd=0
rev=0

while N!=0:
    digit = N%10
    if digit%2!=0:
        odd=odd*10+digit
    N//=10

while odd!=0:
    dig=odd%10
    rev=rev*10+dig
    odd//=10
print("output : ",rev)
