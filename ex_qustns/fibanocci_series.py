n = int(input("enter the number:"))
a,b = 0,1
print(a)
print(b)
for i in range(3,n+1):
    c = a+b
    print(c)
    a,b = b,c
