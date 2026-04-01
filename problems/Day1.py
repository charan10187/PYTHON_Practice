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

# basic
a=10
b=20
print(a,b)
temp=a
a=b
b=temp
print(a,b)
