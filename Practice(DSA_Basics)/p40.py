# problem 40 -- Find the second Smallest Distinct Digit
#   Input  = 5832218
#   Output = 2

nums=list(input())
second=0
sample=[]
smallest=9
for num in nums:
    if num not in sample:
        sample.append(num)
print(sample)
for digit in sample:
    if int(digit)<smalle
        second=smallest
        smallest=int(digit)
print(second)   