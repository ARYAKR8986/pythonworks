tup = (1,1,1,1,2)
f = 1
for i in tup:
    for j in range(i,len(tup)-1):
        if tup[i] != tup[j+1]:
            f = 0
            break
if f==1:
    print("same")
else:
    print("not same")

#another method

tup1 = [2,2,2,2,2]
tup1 = set(tup)
if len(tup) == 5:
    print("same")
else:
    print("not same")