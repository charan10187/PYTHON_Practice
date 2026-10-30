'''
    Problem: 45 -- Find the Most Frequent Distinct Digit
    Input  : 58328218
    Output : 8  
'''

nums=input("Input : ")
freq=-1
largest=9

for num in nums:
    if nums.count(num)>freq and int(num) < int(largest):
        freq=num.count(num)
        largest=int(num)
print(largest)
            