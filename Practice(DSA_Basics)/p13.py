'''
Problem 13 — Count Digits
Input: 4326
Output: 4
'''
n=input("Input: ")
print(len(n))

count=0
for i in range(len(n)):
    count+=1
print(count)
N=int(n)
count=0
while N!=0:
    count+=1
    N=N//10
print(count)