# class A:
#     def displayA(self):
#         print("base class method")
# class B(A):
#     def displayB(self):
#         print("derived class method")
# obj = B()
# obj.displayA()
# obj.displayB()

class Q:
    def read(self):
        self.x = int(input("enter the value:"))
        self.y = int(input("enter the velue:"))
class R(Q):
    def sum(self):
        print("the sum is",self.x+self.y)

ob = R()
ob.read()
ob.sum()