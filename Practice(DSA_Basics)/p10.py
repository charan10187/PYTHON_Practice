# Problem 10 -- Find Factorial
N=int(input("Input: "))
fact=1
for i in range(N,0,-1):
    fact=fact*i
print(f"Output: {fact}")