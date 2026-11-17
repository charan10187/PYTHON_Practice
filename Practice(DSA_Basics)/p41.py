'''
    Problem 41 - Find the second Largest Distinct Digit
    Input = 5832218
    Output = 5
    
'''

nums=input("enter the value : ")

second =-1
largest =-1
result = []

for num in nums:
    if num not in result:
        result.append(num)
for dig in result:
    if int(dig)>largest:
        second=largest
        largest=int(dig)
    elif largest>int(dig) and second<int(dig):
        second=int(dig)
if second==-1:
    print("No second largest distinct digit")
else:
    print(second)


