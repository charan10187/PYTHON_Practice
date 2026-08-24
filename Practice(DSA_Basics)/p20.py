'''
        Problem 20 -- Check if a Number is a Palindrome

'''
# class palindrome:
# def ditrct(N):
#     dup=N
#     rev=0
#     while N!=0:
#         digit=N%10
#         rev=rev*10+digit
#         N=N//10
#     print(rev)
#     print(dup)
#     if rev==dup:
#         return True
#     else:
#         return False
    
    
def slicing(N):
    dup=str(N)
    if dup==dup[::-1]:
        return True
    else:
        return False


N=int(input("enter N: "))
print(slicing(N))
# p1=palindrome()
# print(p1.slicing(N))



        