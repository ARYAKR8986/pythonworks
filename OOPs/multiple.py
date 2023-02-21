class A:
    def employee(self):
        self.x = input("enter the name")
        self.y = input("enter the place")
        self.z = int(input("enter th age"))
class B:
    def salary(self):
        self.p = int(input("enter the salary in January"))
        self.q = int(input("enter the salary in February"))
class C(A,B):
    def display(self):
        print("name is",self.x)
        print("place is",self.y)
        print("age is",self.z)
        print("salary in January is",self.p)
        print("salary in february is",self.q)

obj = C()
obj.employee()
obj.salary()
obj.display()