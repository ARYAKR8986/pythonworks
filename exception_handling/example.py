# try:
#     n1 = int(input("enter the first number:"))
#     n2 = int(input("enter the second numbver:"))
#     n3 = n1/n2
#     print("output is :",n3)
# except ZeroDivisionError as ex:
#     print(ex)
#      OR
# except Valueerror as ex
#     print(ex)

try:
    n1 = int(input("enter the first number:"))
    n2 = int(input("enter the second numbver:"))
    n3 = n1/n2
    print("output is :",n3)
except Exception as exx:
    print(exx)