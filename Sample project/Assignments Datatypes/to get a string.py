# str1 = "restart"
# x = '$'
# str2 = str1.replace(str1[0], x)
#print(str2)

# str3 =
# str4 = str3[0]
# str3 = str3.lower()
# for i in range(1, len(str3)):
#     if
# str3 == 0


sttr = "restart"
char = sttr[0]
length = len(sttr)
sttr = sttr.replace(char, '$')
sttr = char+sttr[1:]
print(sttr)


x = input("enter the word:")
for i in x:
    a = x[0]
    if a==i:
       y=x[1:].replace(i,"$")
print(a+y)