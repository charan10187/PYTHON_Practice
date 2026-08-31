'''
        Problem 35 -- Find the First Non-Repeated Digit
        Input = 112345
        First non- repeated digit = 2

'''
N=list(input("Input = "))
nr=[]

for i in N:
    if N.count(i)==1:
        print(i)
        break
    else:
        print("No non-repeated digit")
