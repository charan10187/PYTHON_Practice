'''
        Problem 37 - Count Frequency of Each Digit
        Input = 5838218
        output = frequency of :
                 5 -> 1
                 8 -> 3
                 3 -> 1
                 2 -> 1
                 1 -> 1 
'''
N=list(input("Input: "))
result=[]

for digit in N:
    if digit not in result:
        print(digit," -> ",N.count(digit))
        result.append(digit)