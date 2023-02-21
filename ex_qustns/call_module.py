import my_module

while True:
    opt = int(input("1.create\n2.search\n3.remove\n4.replace\nEnter your choice:"))
    if opt==1:
        my_module.create()
    elif opt==2:
        my_module.search()
    elif opt==3:
        my_module.remove()
    elif opt==4:
        my_module.replace()
    else:
        break