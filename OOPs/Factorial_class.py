class fact:
    def factorial(self,x):
        f = 1
        for i in range(1,x+1):
            f = f*i
        return f

obj = fact()
x =int(input("enter the number"))
f =obj.factorial(x)
print("factorial is ",f)
#

class Emp:
    def fact(selfsl,n):
        if n == 1:
            return 1
        else:
            return n*selfsl.fact(n-1)
obj = Emp()
n = int(input("enter the number"))
f = obj.fact(n)
print("factorial is ",f)