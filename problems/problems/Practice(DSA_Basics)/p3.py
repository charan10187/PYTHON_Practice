# Problem 3 — Print Even Numbers from 1 to N

N=int(input("N = "))

# for i in range(0,N+1,2):
#     print(i)

for i in range(1,N+1):
    if i%2==0:
        print(i)