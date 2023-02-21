import re
str = 'roses are beautiful and colourful flowers'
s = re.findall('roses',str)
print(s)
#
# s1 = re.findall('rosess',str)
# print(s1)


# q = re.findall('[scr]a',r)
# # print(q)
# d = 'mat rat pat sat cat'
# q = re.findall('[^scr]a',d)
# print(q)
#
#
# r = 'cat mat rat sat pat 9985 969'
# q = re.findall('\d{3}',r)
# print(q)
#
# q= 'cat mat rat 99998 666 3455 123455 1234556'
# w = re.findall('\d{1,4}',q)
# print(w)

t= 'cat mat rat 99998 666 3455'
e = re.findall(r'\b\d{4}\b',t)
print(e)