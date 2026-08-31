'''
        Problem 34 -- Find the First Repeated Digit
        Input = 123245
        First repeated digit = 2

'''
N=list(input("Input = "))
repeat=[]
for i in range(len(N)):
    for j in range(len(N)):
        if i!=j and N[i]==N[j]:
            if N[i] not in repeat:
                repeat.append(N[i])
print("Count = ",repeat[0])


        
               