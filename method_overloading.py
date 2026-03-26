# class MultiCls:
#     def add(self,*args):
#         return sum(args)
# c1=MultiCls()
# print(c1.add(10,20,30,40))
class Multi:
    def __init__(self,*args):
        self.args=args
    def add(self):
        total=0
        for i in self.args:
            total=total+i
        return total
c1=Multi(10,20,30,40)
print(c1.add())