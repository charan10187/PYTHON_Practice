'''

# Exercise 1
numbers=[10,20,30,40,50]
for num in numbers:
    print(num)

# Exercise 2
numbers=[10,20,30,40,50]
for num in numbers:
    if num==20:
        print(num)
    if num==40:
        print(num)

# Exercise 3
numbers=[10,20,30,40,50]
new=[]
for i in numbers:
    if i<40:
        new.append(i)
print(new)

# Exercise 4
numbers=[10,20,30,40,50]

for i in range(len(numbers)):
    print("Index",i,"=",numbers[i])

# Exercise 5
numbers=[10,20,30]
for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(numbers[i],numbers[j])

# Exercise 6
numbers=[1,2,2,3]
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i!=j and numbers[i]==numbers[j]:
            print(numbers[i],numbers[j])
           
'''
# Exercise 7
numbers=[1,2,2,3]
count=0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i!=j and numbers[i]==numbers[j]:
            count+=1
print("count = ",count)