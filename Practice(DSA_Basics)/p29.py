'''
        Problem 29 -- Count Digit Equal to thrLargest Digit
        Input = 58382
        Largest digit = 8
        count = 2 
'''

N=int(input(" Input = "))
dup=N
big=0
count=0

while N!=0:
    digit=N%10
    if digit>big:
        big=digit
    N//=10
while dup!=0:
    digit=dup%10
    if digit==big:
        count+=1
    dup//=10
print("largest digit = ",big)
print('count = ',count ) 