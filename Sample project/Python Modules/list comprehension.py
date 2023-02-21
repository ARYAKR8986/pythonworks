#print([x for x in "hello world"])


q = ("orange","apple","grape","kiwi","cherry")
w = [x for x in q if "a" in x]
print(w)

#
# letters = [letter for letter in "human"]
# print(letters)
#
#
# r = [num for num in range(101) if num%2==0]
# print(r)



#$print(sum(i for i in range(11)))

print(sum([i for i in range(1,int(input("enter the range")))]))

#print([(n*(n+1)/2) for n in range])