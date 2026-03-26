class MultiCls:
    def add(self,*args):
        return sum(args)
c1=MultiCls()
print(c1.add(10,20,30,40))