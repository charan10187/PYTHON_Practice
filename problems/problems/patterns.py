#n=int(input("Enter a number: "))
def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print(" ")

def pattern2(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print(" ")

def pattern3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print(" ")

def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print(" ")

def pattern5(n):
    for i in range(n+1):
        for j in range(1,n-i+1):
            print("*",end=" ")
        print(" ")

def pattern6(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print(i,end=" ")
        print(" ")

def pattern7(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print(j,end=" ")
        print()
pattern6(4)
 