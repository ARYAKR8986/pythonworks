
"""factorial of a number using function with return type and function parameter"""


def fact(n):
    f = 1
    for i in range(1, n+1):
        f=f*i
    return f

g = fact(5)
print("factorial is:",g)