'''
        Problem 39 -- Find the Smallest Repeated Digit
        Input = 5832218

'''

N=list(input('Input = '))
smallest=9
result=[]
key=[]
value=[]
for digit in N:
    # print(digit)
    if digit not in result:
        if N.count(digit)>1:
        # print(digit)
            key.append(digit)
            value.append(N.count(digit))
            result.append(digit)
index=-1
for i in range(len(value)):
    # print(i)
    # if value[i]>1:
        # print(value[i])
        if value[i]<smallest:
            smallest=int(value[i])
            index=i
            print(smallest , value)
print(key[i])
# print(value[i])
# print(value)
# print(key)
# if index==-1:
#     print("no repeat")
# else:
#     print(key[index])


    