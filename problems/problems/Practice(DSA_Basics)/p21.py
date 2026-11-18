'''
        Problem 21 -- Sum of Even Digits
        Input = 123456
        Sum of even digits = 12
'''

N=int(input("Input = "))
total=0
while N!=0:
    digit=N%10
    if digit%2==0:
        total=digit+total
    N=N//10
print(total)


