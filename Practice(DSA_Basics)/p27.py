"""
        Problem 27 -- Count Digit Greater Than the Average
        Input = 12345
        Count=2
        ( 4,5 )
"""

N=int(input("Input = "))
n=str(N)
total=0
count=0
dup=N
while N!=0:
    digit=N%10
    total=digit+total
    N//=10
# print(total)
# print(len(n))
result=int(total/len(n))
# print(result)
while dup!=0:
    digit2=dup%10
    dup//=10
    # print(digit2)
    # print(result)
    if digit2>result:
        count+=1
print("count =",count)