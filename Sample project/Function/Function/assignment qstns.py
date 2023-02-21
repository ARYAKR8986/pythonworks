# def multiply(num):
#     total = 1
#     for i in num:
#         total *= i
#     return total
# print(multiply((1,3,4,6,7)))
#
#
#
# #
def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * fact(n-1)
n =5
print( fact(5))
fact(n)

#
#
#
#
#
#
# n = 5
# if n>1:
#     for i in range(2,int(n/2)+1):
#         5 n%i ==0
#     print(num,"is not a prime number")
#     else:
#     print(num,"is a prime number")













#addition func











# t =int(input("enter the start position"))
# finish =int(input("enter the finishing position"))
# a = []
# for i in range(a,b,2):
#     a.append(i)






def prime(x):
    if x==1:
        print("1 is neither prime nor consecutive")
    elif x<1:
        print("please enter a positive value")
    elif x==2:
        print("2 is prime number")
    else:
        flag = 1
        for j in range (2,x):
            if x % j ==0:
                flag = 0
                break
            else:
                continue
        if flag == 0:
            print(f,"the number {x} is not prime")
        else:
            print(f,"the number {x} is prime")
num = int(input("enter the number"))
print(num)