from abc import ABC, abstractmethod
#abstract class
class polygon(ABC):
    #abstrsct method
    @abstractmethod
    def sides(self):
        pass
    def display(self):
        print("non abstract method")
class triangle(polygon):
    def sides(self):
        print("triangles has 3 sides")
ob = triangle()
ob.sides()
ob.display()