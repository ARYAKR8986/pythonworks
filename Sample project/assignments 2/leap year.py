n = int(input("enter the year"))
if (n%400 == 0) and  (n%100 == 0):
    print("the year is leap year")
elif (n%4 ==0) and (n%100!=0):
    print("the year is  leap year")
else:
    print("the year is not leap year")