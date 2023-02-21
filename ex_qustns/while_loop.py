#reverse of a number using while

n = 123
rev = 0
while n>0:
    r = n%10
    rev = rev*10+r
    n = n//10
print("reverse is:",rev)

#product of digits

q = 23459
rev = 0
p = 1
s = 0
while n>0:
    r = n%10
    p = r*p
print("product is:",p)