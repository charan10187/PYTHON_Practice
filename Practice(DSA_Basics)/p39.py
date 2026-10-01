'''
        Problem 39 -- Find the Smallest Repeated Digit
        Input = 5832218
        output = 2

'''

N=list(input('Input = '))
smallest=9
result=[]
key=[]
value=[]
for digit in N:
    if digit not in result:
        if N.count(digit)>1:
            key.append(digit)
            value.append(N.count(digit))
            result.append(digit)
index=-1
for i in range(len(key)):
    if int(key[i])<smallest:
        smallest=int(key[i])
        index=i
        # print(smallest , value)
if index==-1:
    print('no repeat')
else:
    print(key[index])



    