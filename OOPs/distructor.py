class A:
    def __init__(self,name):
        print("paraconstructor")
        self.na = name
    def __del__(self):
        print("distructor")
    def display(self):
        print("name is",self.na)
obj = A('Anu')
obj.na
obj.display()