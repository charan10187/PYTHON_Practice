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

'''

# Exercise 4
numbers=[10,20,30,40,50]

for i in range(len(numbers)):
    print("Index",i,"=",numbers[i])
