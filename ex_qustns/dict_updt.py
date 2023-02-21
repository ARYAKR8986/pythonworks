# d = {}
# number = int(input("enter the number of elements in the dictionary:"))
# for i in range(number):
#     key = int(input("enter the  key:"))
#     value = input("enter the value:")
#     d.update({key:value})
# print(d)

#to get only keys

x = {"colour":"blue","fruit":"apple"}
for i in x.keys():
    print(i)

for i in x.values():
    print(i)

for i,j in x.items():
    print(i,j)

q = x.get("fruit")
print(q)