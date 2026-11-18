# Exception handling

try:
    a=9
    b=0
    print(a/b)
except ZeroDivisionError :
    raise NameError

finally:
    print("complte")