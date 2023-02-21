#list of square num b/w 1 to 30

def squarevalues():
    l = list()
    for i in range(1,31):
        l.append(i**2)
    print(l)
squarevalues()

#deffrnt name call thrgh new name

def details (name,place):
    print(name,place)
details("Thiago","Brazil")
details_new = details
details_new("Thiago","Brazil")

  #or

def func1():
    print("name")
func1 = func2
func1()

