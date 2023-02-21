# #even nuumbers between 4 to 30

start = int(input("enter the starting position:"))
stop = int(input("enter the stop position"))
def even():
    v=[]
    for i in  range (start,stop):
        if i%2 ==0:
            print(i)
            v.append(i)
    print()
even()

