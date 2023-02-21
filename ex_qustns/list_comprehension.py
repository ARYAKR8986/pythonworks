#list comprehension

#syntax -

# l = [x+3 for x in [1,2,3,4]]
# print(l)
# q= [x%2==0 for x in range (1,26)]
# print(q)
#
# l = [i for i in range(25) if i%2==0]
# print(l)
#
# s = [i for i in  'malayalam' if i in  ['a','e','i','o','u'] ]
# print(s)


#split

# t = input("enter the string:")
# words = t.split( )
# firstletter = [i[0] for i in  words]
# print(firstletter)

# colors = ['red','white','green','pink']
# lettere = [i for i in colors if 'e' in i]
# print(lettere)

# colours = ['white','green','pink','blue']
# letterg = [ i for i in colours if i!='green']
# print(letterg)
#
# colors1 = ['yellow','red','blue']
# upper = [i.upper() for i in colors1]
# print(upper)
#
# colors2 = ['rose','black','silver']
# change = ["hello" for i in colors2]
# print(change)

colors3 = ['white','red','green','pink']
newcolor = [i if i!='pink' else 'blue' for i in colors3]
print(newcolor)