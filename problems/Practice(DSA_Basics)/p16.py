'''

Problem 16 -- Count Digits Greater Than 5

'''

N=int(input("Input: "))
count=0
while N!=0:
    digit=N%10
    if digit>5:
        count+=1
        # print(digit)  
    N=N//10
print(count)

