list1 = ["a","b",["c",["d","e",["f","g"],"k"],"m","n"]
list2 = ["h","i","j"]
for i in list2:
    list1[2][1][2].append(i)
print(list1)