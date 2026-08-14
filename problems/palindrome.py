'''str1=input("enter the string:")
if str1==str1[::-1]:
    print("Palimdrome")
else:
    print("Not Palindrome")
'''
s=input("enter the string:")
rev=""
for i in s:
    rev=i+rev
print("palindrome" if s == rev else "not palindrome")
