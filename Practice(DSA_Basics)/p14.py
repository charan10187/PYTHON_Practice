'''
    Problem 14 -Sum of Digits
    Input: 23456
    Output: 20
'''

N=int(input("Input: "))
total=0

# Using while loop 

while N!=0:
    dig=N%10
    total=dig+total
    N=N//10
print(total)

# Using for loop

for i in range(len(str(N))):
    val=N%10
    total=val+total
    N=N//10
print(total)