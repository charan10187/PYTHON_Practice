'''
        Problem 36 - Finding the Largest Repeated Digit
        Input = 5838218
        Largest repeated digit = 8
'''

N=list(input("Input :"))
result=[]
largest=0
for digit in N:
    if N.count(digit)>1:
        print(digit)
