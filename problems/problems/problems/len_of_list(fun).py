lst=[10,20,30,40,50]
"""def length(a):
    b=len(a)
    print("length of array")
    print(b)
length(lst=[input()])"""
def single(lst):
    for i in range(len(lst)):
        if i==len(lst)-2:
            break
        print(lst[i],end="")
        print(",")
single(lst)