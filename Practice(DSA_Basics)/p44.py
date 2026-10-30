'''
    Problem 44: Find the Third Smallest Distinct Digit
    Input  : 5832218
    Output : 3
'''
nums=input("Input : ")
result=[]
first=9
second=9
third=9

for num in nums:
    if num not in result:
        result.append(num)
for i in result:
    num=int(i)
    if num<first:
        third=second
        second=first
        first=num
    elif num<second:
        third=second
        second=num
    elif num<third:
        third=num
if third==9:
    print("Output: No third smallest distinct digit")
else:
    print(f"Output: {third}")