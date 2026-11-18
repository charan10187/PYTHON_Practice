''''
            Problem 22 -- Sum of Odd Digits
            Input = 123456
            Sum of Odd digits = 9

'''

N=int(input("Input = "))
total=0
while N!=0:
    digit=N%10
    if digit%2!=0:
        total+=digit
    N=N//10
print(total)