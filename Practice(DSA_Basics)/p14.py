'''
    Problem 14 -Sum of Digits
    Input: 23456
    Output: 20
'''

N=int(input("Input: "))
sum=0
for i in range(len(str(N))):
    val=N%10
    sum=val+sum
    N=N//10
print(sum)