'''
        Problem 42 -- Finding the Third Largest Distinct Digit
        Input = 5832218
        Output = 3

'''

# take values 5 8 8 3 2 1

# check for duplicates using a empty list  5 8 3 2 1 

# iterate the list with the condition num >first

# if condition satisfied update the fist=num and second=first and third =second

nums=input("Input: ")

first=-1
second=-1
third=-1
result=[]
for num in nums:
    if num not in result:
        result.append(num)
for dig in result:
    num=int(dig)
    if num> first:   
        third=second
        second=first   
        first=num      
    elif num>second:
        third=second
        second=num
    elif num>third:
        third=num
if third==-1:
    print("No third largest distinct digit")
else:
    print(third)
        



