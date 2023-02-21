def make_pretty (func):

    def inner():
        print()
        func()
    return inner()

@make_pretty
def ordinary():
    print("i am ordinary")
