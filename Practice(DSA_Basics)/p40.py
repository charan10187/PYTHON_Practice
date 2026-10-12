# problem 40 -- Find the second Smallest Distinct Digit
#   Input  = 5832218
#   Output = 2

nums=list(input("Input:"))
second=10
sample=[]
smallest=9
for num in nums:
    if num not in sample:
        sample.append(num)
print(sample)
for digit in sample:
    if int(digit)<smallest:
        second=smallest
        smallest=int(digit)
    elif int(digit)<second:
        second=int(digit)
print(second)   