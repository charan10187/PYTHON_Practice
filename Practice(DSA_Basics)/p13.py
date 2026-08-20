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
''' 
For the edge case (Input: 0 ) the above two approches will fail besacuse len(0) is countes as an element it retuens the Output as 1 
'''
N=int(n)
count=0
while N!=0:
    count+=1
    N=N//10
print(count)