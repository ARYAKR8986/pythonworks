row = int(input("enter the value"))

for i in range(row):
    for j in range(i+1):
        print(j+1, end=" ")
    print()


r = int(input("enter the numebr"))
for i in range(r):
    for j in range(r+i):
        print()
