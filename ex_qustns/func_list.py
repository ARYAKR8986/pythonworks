# l = []
# def create():
#     number = int(input("enter the number of elments in the list:"))
#     for i in range(number):
#         item = int(input("enter the item:"))
#         l.append(item)
#         print(l)
# create()
#
# t = [2,3,4,5]
# def search():
#     item = int(input("enter the tem to be searched:"))
#     if item in t:
#         print("item found")
#     else:
#         print("item not found")
# search()
#
#
# q = [1,2,4,5]
# def remove():
#     item2 = int(input("enter the item to be removed:"))
#     if item2 in q:
#         q.remove(item2)
#     else:
#         print("item not found in list")
#     print(q)
# remove()


#replace
w = [3,6,9,0]
def replace():
    old = int(input("enter the item to be replace:"))
    new = int(input("enter the new item replaced:"))
    for i in range(len(w)):
        if w[i]==old:
            w[i]=new
    print(w)
replace()

while True:
    opt = int(input("1.create\n2.search\n3.remove\n4.replace\nEnter your choice:"))
    if opt==1:
        create()
    elif opt==2:
        search()
    elif opt==3:
        remove()
    elif opt==4:
        replace()
    else:
        break