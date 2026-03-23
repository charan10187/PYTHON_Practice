class pointer:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,new):
        return self.a + new.a + self.b + new.b
p1=pointer(2,4)
p2=pointer(3,2)
print(p1+p2)