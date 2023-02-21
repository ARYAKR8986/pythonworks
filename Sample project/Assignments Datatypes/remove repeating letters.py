str = "let's google the pineapple"
str1 = str.split(' ')
str2 = []
for i in str1:#lets, google, the, pineapple
    l = ""
    for j in i:#l, e, t, ', s
        if j in l:
            continue
        else:
            l = l+j
    str2.append(l)
print(' '.join(str2))
