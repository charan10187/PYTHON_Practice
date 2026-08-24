'''
        Problem 19 -- Count a Special Digit
        Number = 12234252
        Target digit = 2 
'''

def count(N,T):   
    count=0
    while N!=0:
        digit=N%10
        if digit==T:
            count+=1
        N=N//10
    return count

N=int(input("Number = "))
T=int(input("Target = "))
print(count(N,T))









