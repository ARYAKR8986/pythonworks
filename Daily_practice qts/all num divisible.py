"""program to print all numbers in a range divisible by a number"""

lower = int(input("enter the lower range number:"))
upper = int(input("enter the upper range number:"))
n = int(input("enter the numb er to be devided by:"))
#the reminder of number devided by i is equal to 0, i is printed
for i in range (lower,upper+1):
    if (i%n == 0):
        print(i)