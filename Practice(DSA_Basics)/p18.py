'''
        Problem 18 -- Find the Smallest Digit

        Input : 58321
        Output: 1

'''

n=int(input("Input : "))
small=n
while n!=0:
    digit=n%10
    if digit<small:
        small=digit
    n=n//10
print(small)
