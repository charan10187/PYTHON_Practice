'''
    Problem 38 - Find the most Frequent Digit
'''

N=list(input("Input = "))
largest=9
result=0
for num in N:
    digit=N.count(num)
    if digit<largest or digit>largest:
        largest=digit
        result=num
print(result)

        