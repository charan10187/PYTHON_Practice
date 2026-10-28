'''
        Problem 42 -- Finding the Third Largest Distinct Digit
        Input = 5832218
        Output = 3

'''

# take values 5 8 8 3 2 1

# check for duplicates using a empty list  5 8 3 2 1 

# iterate the list with the condition num >first

# if condition satisfied update the fist=num and second=first and third =second


from os import remove


nums=[5,8,8,3,2,1]

result=[]
for num in nums:
    if num not in result:
        result.append(num)
for i in range(1,len(result)):
    if result[i]>result[0]:
        remove(result[i])
for j in range(len(result)):
    if result[0]>result[j]:
        print(result[j])







