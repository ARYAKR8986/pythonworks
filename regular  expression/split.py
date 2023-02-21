import re

str='class will start at 10am'
s = re.split(" ",str)
print(s)

s = re.split("a",str)
print(s)

s = re.split("a",str,2)
print(s)

#fullmatch

w = 'python is a language'
r = re.fullmatch(w,'python is a language')
print(r)

t = re.match(w,"python is a language")
print(t)

#sub()

input = 'rose and jasmine are flowers'
g = re.sub(' ','*',input)
print(g)

g = re.sub(' ','*',input,2)
print(g)

