'''num=1231
s=str(num)
if s==s[::-1]:
    print("palindrome")
else:
    print("Not palindrone")
    '''
num=12321
temp=num
rev=0
while num>0:
    r=num%10
    rev=rev*10+r
    num=num//10
print("palindrome" if temp==rev else "Not a palindrome")
    