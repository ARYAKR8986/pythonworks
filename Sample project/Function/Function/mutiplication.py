#multiplication

def mul (lis):
    m=1
    for i in lis:
        m = m*i

    return m
list1 = [1,2,3,4]
print(mul(list1))


#reverse

def reverse (str1):
    return  str1[::-1]
str1 = "124abc"
print(reverse(str1))