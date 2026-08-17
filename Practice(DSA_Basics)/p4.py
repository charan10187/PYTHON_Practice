# Problem 4 — Print Odd Numbers from 1 to N

N=int(input("N = "))
# for i in range(1,N+1,2):
#     print(i)

# for i in range(0,N+1):
#     if i%2!=0:
#         print(i)

a=1
for i in range(N):
    print(a)
    a=a+2

# using this approuch we cant get all Odd Numbers
# a=1
# b=1
# temp=0
# for i in range(0,N+1):
#     a=b   
#     b=temp        
#     temp=a+b   
#     print(temp)


