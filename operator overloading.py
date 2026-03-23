class pointer:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a + self.b
p1=pointer(2,3)
p2=pointer(8,4)
print(p1.add(),p2.add())