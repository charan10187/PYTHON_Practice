''''
        Problem 23 -- Product of Digits
        Input = 1234
        Product of digits = 24
'''

N=int(input("Input = "))
total=1
while N!=0:
    digit=N%10
    total=total*digit
    N//=10
print(total)



