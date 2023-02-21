def fact(n):
    if (n==1):
        return 1
    else:
        return n * fact(n-1)
    print(n)
n =5
print( fact(5))
fact(n)


def natural(n):
    if (n==1):
        return 1
    else:
        return n*(n+1)/2
n=6
print(natural(6))
natural(n)