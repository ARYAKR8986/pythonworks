n = int(input("enter the num:"))
count = 0
i = 2
while i < n:
    if n % i == 0:
        count = 1
        print(n," is not prime")
    i = i + 1
if count == 0:
        print(n, "is prime")