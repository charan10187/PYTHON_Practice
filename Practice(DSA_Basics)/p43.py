'''
    problem 43 -- Find the Second Smallest Distinct Digit Using Third variable
    Input = 5832218
    Output = 2

'''

nums=input("Enter the Input: ")

second=9
first=9
result=[]
for num in nums:
    if num not in result:
        result.append(num)
for num1 in result:
    num=int(num1)
    if num<first:
        second=first
        first=num
    elif num < second:
        second = num
if second==9:
    print("No second smallest didtinct digit")
else:
    print(second)