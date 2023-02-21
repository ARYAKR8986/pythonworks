"""Write a program to print characters from """

str1 = input("enter the string")
print("The string is",str1)
l = len(str1)
print("characters at even index number are:")
for i in range(0,l,2):
    print(str1[i])