class A:
    def __init__(self,name):
        print("parameterised consructor")
        self.na = name
    def display(self):
        print("name is",self.na)
obj = A('arun')
obj.display()