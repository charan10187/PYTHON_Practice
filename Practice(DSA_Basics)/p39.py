'''
        Problem 39 -- Find the Smallest Repeated Digit
        Input = 5832218

'''

N=list(input('Input = '))
largest=-1
smallest=9
result=[]
key=[]
value=[]
for digit in N:
    if digit not in result:
        key=digit
        value=N.count(digit)
        result.append(digit)
print(value)
print(key)



    