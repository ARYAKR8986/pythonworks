# class Employee:
#     x = 100
#     def display(self):
#         print("the employee is")
#
# obj = Employee()
# obj.display()
# print("value of x is ",obj.x)
#
# obj =Employee()#calling object without function bracket, no need to give 'self' parameter inside 'display'
# obj.display()
#


# class numbers:
#     def display(self):
#         print('simple function')
#     def sum(self,a,b):
#         print('sum is ',a+b)
#     def product(self,a,b):
#         print("product is ",a*b)
#
# obj = numbers()
# obj.display()
# obj.sum(2,3)
# obj.product(4,6)

# '******'
#
class exmp:
    def read(self,a,b):  #OR    #self(a,b)
        self.x = a              #self.a = a
        self.y = b              #self.b = b
    def sum(self):
        print('sum is ',self.x + self.y)  #(self.a+self.b)
    def prdct(c):
        print("product is ",c.x * c.y)  #(c.a+c.b)
obj = exmp()
obj.read(3,6)
obj.sum()
obj.prdct()

