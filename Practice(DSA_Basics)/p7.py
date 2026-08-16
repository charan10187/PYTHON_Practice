# Problem 7 --Find the largest of three Numbers
A=int(input())
B=int(input())
C=int(input())
if A>=B and A>=C:
    print("A")
elif B>=A and B>=C:
    print("B")
elif C>=A and C>=B:
    print("C")
