'''
 Problem 15 — Count Even and Odd Digits

    Input:123456
    Output:
            Even digits = 3
            Odd digits = 3

 '''

N=int(input("Input:"))
count=0
even=0
odd=0
while N!=0:
    digit=N%10
    if digit%2==0:
        even=count
        count+=1
    else:
        odd=count
        count+=1
    N=N//10
print(even)
print(odd)


