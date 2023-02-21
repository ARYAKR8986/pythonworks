str1 = ("/*Jon is @ developer & musician!!")
rmv = ('/','*','@','&','!')
for letter in rmv:
    str1 = str1.replace(letter,"#")
print(str1)