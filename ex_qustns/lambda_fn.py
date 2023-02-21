def sum(a,b):
    return a+b
print(sum(3,6))

#using lambda function

#syntax - lambda arguments:expression
add = lambda a,b:a+b
print(add(5,7))

largest = lambda a,b:a if (a>b) else b
print(largest(200,100))


#filter,map,reduce

#filter
l = [12,13,56,35,78,97,24]
list1 = list(filter(lambda x:x%2==0,l))
print(list1)

#lambda
m = [56,87,0,53,23,56,78]
list2 = list(map(lambda y:y*2,m))
print(list2)

#reduce
from functools import reduce

l3 = [1,2,3,4,5]
product = reduce(lambda x,y:x*y,l3)
print(product)