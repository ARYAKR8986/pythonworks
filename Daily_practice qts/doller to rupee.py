'''dictionary comprehension'''

def doller_to_rupee():
    """create a new dictionary"""
    price = {'laptop':10,'mobile':5,'watch':3,'keyboard':1}

    """multiplied the price and convert to  rupee
    convert to rupee = one doller convert to indian rupee"""

    convert_to_rupee = 81.38
    n_price = {i: j*convert_to_rupee for (i,j) in price.items()}
    return n_price
rc = doller_to_rupee()
print(rc)