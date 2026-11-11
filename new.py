# cars=["porsche","ferrari","lamborghini"]
# trending=[]
# for car in cars:
#     if car == "porsche" or car == "ferrari":
#         trending.append(car)
# print(trending)
# print(3*1**3)


class parent:
    def mom(self):
        print("parent")
class child(parent):
    def son(self):
        print("coming")

c=child()
c.mom()