class rectangle:
    def area(self,l,b):
        print("area is",l*b)
class square(rectangle):
    def area(self,l,b):
        print("area is",l*b)
obj = square()
obj.area(10,20)






#if signature, function name all are same of two differnt classes then derived
#class overrides base class metod