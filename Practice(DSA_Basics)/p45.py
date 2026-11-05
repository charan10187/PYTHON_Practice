'''
    Problem: 45 -- Find the Most Frequent Distinct Digit
    Input  : 58328218
    Output : 8  
'''

nums=input("Input : ")
freq=1

duplicate=[]
for num in nums:
    if num not in duplicate:
        duplicate.append(num)
for num1 in duplicate:
    if num1 in nums:
        ct=nums.count(num1)
        if ct>freq:
            freq=ct
            large=num1
if freq == 1:
    print("Any digit (all have frequency 1)")
else:
    print(large)
            