# Problem 12 --Reverse a Number
N=int(input("Input: "))
rev=0
# while N!=0:
for i in range(len(str(N))):
    lastD=N%10
    rev=lastD+rev*10
    N=N//10

print("Output:",rev)