str1 = ["john","","jack","emma","","jins","lina"]
for i in str1 :
    if(len(i)==0):
        str1.remove(i)
print("str1 =",str1)