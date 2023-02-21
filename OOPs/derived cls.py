class A:
    def number(self):
        self.x = int(input("enter the number"))
        self.y = int(input("enter the number"))
class B(A):
    def sum(self):
        print("the sum is:",self.x+self.y)
class C(B):
    def average(self):
        print("the average is",(self.x+self.y)/2)
obj = C()
obj.number()
obj.sum()
obj.average()