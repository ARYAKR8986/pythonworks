def outeradd(a,b):
    def inneradd(a,b):
        return a+b
    return(inneradd(a,b)+5)
print(outeradd(2,3))