'''
        Problem 25 -- Second Largest Digit
        Input = 58321
        Second largest digit =5

'''

N=int(input("Input = "))
old=-1
new=-1

while N!=0:
    digit=N%10
    if digit>new:
        new=old
        old=digit
    N//=10
print("second Largest digit",old)