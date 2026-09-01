'''
        Problem 36 - Finding the Largest Repeated Digit
        Input = 5838218
        Largest repeated digit = 8
'''

N=list(input("Input :"))
result=[]
largest=0
for digit in N:
    # print(digit)
    if digit not in result:
        if N.count(digit)>1:
            result.append(digit)
            demo=int(digit)
            if demo>largest:
                largest=demo
print(largest)

