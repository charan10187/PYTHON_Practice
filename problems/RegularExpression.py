# Regular Expression 
# import re
# z="python"
# t=re.


# x='1234df@'
# if x.isalnum():
#     print("a")
# x=[1,2,3,4,5]
# x[0],x[-1]=x[-1],x[0]
# print(x)
# x='pYTHon'
# y=x.swapcase()
# print(y)
# x="python is oOPwerfghj laNGuage"
# y=x.split(" ")
# print(y)
# result=''
# small=-1
# for i in y:
#    if len(i)>small:
      
#       small=len(i)
#       result=i
      
# print(result)
'''x='python is oOPwerfghj laNGuage'
result=[]
final=[]
for ch in x:
   if x.count(ch) >1:
      if ch not in result:
        result.append(ch)
result.remove(' ')
# for ch in result:
#     if ch in result:
#        final.append(ch) 
print(result)'''

name='charan'
dname=''
for ch in name:
    if ch in 'aeiou':
        # print(ch)
        ch='%'
    dname=dname+ch
print(dname)