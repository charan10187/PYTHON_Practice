'''
        Problem 28 -- Count Digit Smaller Then the Average
        Input = 12345
        Count = 2
'''

N=int(input("Input = "))
dup=N
count=0
total=0
# loop for total Digits
while N!=0:
    digit=N%10
    total=digit+total
    N//=10
# count of digits in input
result=total/len(str(dup))

# loop for count digits lessthen average
while dup!=0:
    digit2=dup%10
    if digit2<result:
        count+=1
    dup//=10
print('count = ',count)