#add list of elements

a = [2,3,4,5]
c = {2,3,6,9}
c.update(a)
print(c)

#unique items from two sets

set1 = {2,3,6,7,9}
set2 = {2,7,4,5,0}
print(set1.union(set2))
     #or
w = set1|set2
print(w)

#display common elements

set3 = {2,3,6,7,9}
set4 = {2,7,4,5,0}

if set3.isdisjoint(set4):
    print("two sets have no elements in common")
else:
    print("two sets have elements in common")


#remove items from set1

set5 = {2,3,6,7,9}
set6 = {2,7,4,5,0}
set5.intersection_update(set6)
print(set5)