# swaping of two numbers
"""
logic:
take a,b values
create a third variable ex:temp
store the a or b value in temp
temp=a
then assine b value to a , here a becomes b 
then assine b=temp where temp is holding the a value so b becomes a
 """

# basic level
"""
a=10
b=20
print(a,b)
temp=a
a=b
b=temp
print(a,b)

"""
# # intermediat level
# 
# a=input("a :")
# b=input("b :")
# print(f"before swaping {a},{b} values")
# temp=a
# a=b
# b=temp
# print(f"After swaping a:{a},b:{b}")

# Advanced level
'''
a,b=map(int,input().split())
print("before swap",a,b)
temp=a
a=b
b=temp
print("After swap",a,b)
'''
# # without using third variable
# a,b=map(int,input("enter a,b values: ").split())
# print(f"a:{a},b:{b}")
# a=a+b
# b=a-b
# a=a-b
# print(f"a:{a},b:{b}")

# without logic
a, b = input().split()
print(f"before swapping {a},{b} values")
a, b = b, a
print(a, b)