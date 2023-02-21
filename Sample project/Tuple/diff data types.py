tple =(2,3,6,7,"name",9.7,"xox")
print(tple)
print(tple[1]) #index vlue
print(tple[::-1]) #reversing
print(tple[:-3])
print(tple[0:-3])
print(tple[-3:-6])

#updating of tuple

tple1 = (2,3,4,5,"name","place","good")
y = list(tple1)
y[0] = "school"
print(y)

#append

tple2 =(1,2,3,"apple","orange","grape")
s = list(tple2)
s.append("lemon")
tple2 = tuple(s)
print(tple2)

#adding

tple3 = (2,6,7,"rome","paris","italy")
w =("lee","jmmu")
tple3 += w
print(tple3)

#removing

tple4 = (2,3,7,"tree","bush","fern")
x = list(tple4)
x.remove("bush")
tple4 =tuple(x)
print(tple4)

#del

tple5 = (2,3,7,"tree","bush","fern","fish")
del tple5
print(tple5)

