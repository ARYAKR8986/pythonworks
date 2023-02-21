a = [1,2,3,4,5]
b = enumerate(a)
print(b)

name = ['mukesh','tony','ronyr']
age = [20,26,67]
for i,(name,age) in enumerate(zip(name,age)):
    print(i,name,age)

letters = [('a','A'),('b','B')]
for i, letters in enumerate(letters):
    print("letter %d is %s/%s",letters)


x = ['mat','cat','rat','bat']
y = list(map(tuple,x))
print(y)

w = list(map(set,x))
print(w)

c = list(map(list,x))
print(x)