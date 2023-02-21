a = 2
b = 6
t = a
a = b
b = t
print(a)

a,b = int(input("enter the number")),int(input("enter the number"))
a,b = b,a
print("a=",a)
print("b=",b)