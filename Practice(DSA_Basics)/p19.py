'''
        Problem 19 -- Count a Special Digit
        Number = 12234252
        Target digit = 2 
'''

def count(N,T):   
    total=0
    while N!=0:
        digit=N%10
        if digit==T:
            total+=1
        N=N//10
    return total

N=int(input("Number = "))
T=int(input("Target = "))
print(count(N,T))









