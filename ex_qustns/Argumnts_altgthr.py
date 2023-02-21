def student(x,*args,**kwargs):
    print("simple argument is:",x)
    for j in args:
        print(j)
    for i,j in kwargs.items():
        print('%s=>%s'%(i,j))

student('Amal','Varun','Sini',st2= 'Anu',st3='Vini',st1='Raman')