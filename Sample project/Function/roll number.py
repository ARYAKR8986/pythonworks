def check(roll):
    a =[12,24,36,48,56]
    if roll in a:
        print("this student is present")
    else:
        print("this student is absent")
roll =int(input("enter the roll number"))
check(roll)