#factorial

n = int(input("enter the number"))
p = 1
i = 1
while i <= n:
    p = p*i
    i = i+1
print("factorial of %d is %d"%(n,p))
