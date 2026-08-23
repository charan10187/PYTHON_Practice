'''
        Problem 17 -- Find the Largest Digit

        Input= 58321
        Output= 8 
'''
n=int(input("Input: "))

largest=0
while n!=0:
    digit=n%10
    if largest<digit:
        largest=digit
    n=n//10
print(largest)
    