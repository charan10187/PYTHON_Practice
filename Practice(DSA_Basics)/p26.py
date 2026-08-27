'''
    Problem 26 -- Find the Smallest and Largest Digit
    Input = 58321
    Largest digit = 8
    Smallest digit = 1

'''
N=int(input("Input = "))
large=0
small=9
while N!=0:
    digit=N%10
    if digit>large:
        large=digit
    if digit<small:
        small=digit
    N//=10
print(large,small)
