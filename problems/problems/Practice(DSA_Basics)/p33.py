'''
        Problem 33 -- Count Digit That Appear More than Once
        Input = 122343
        Count = 2 

'''
N=list(input("Input = "))
repeat=[]
for i in range(len(N)):
    for j in range(len(N)):
        if i!=j and N[i]==N[j]:
            if N[i] not in repeat:
                repeat.append(N[i])
print("Count = ",len(repeat))

