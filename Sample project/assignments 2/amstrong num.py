# n = int(input("enter the number:"))
# sum == 0
# power = len(str(n))
# p = n
# while p > 0:
#     digit = p%10
#     sum += digit**power
# if n==sum:
#     print(n,"is an armstrong number")
# else:
#     print(n,"is not an armstrong number")

n = int(input("enter the num:"))
p = n
q = len(str(n))
sum = 0
while n > 0:
    r = n % 10
    sum = sum+(r**q)
    n = n//10
if p == sum:
    print( p, "is armstrong number")
else:
    print( p, "is not armstrong number")
