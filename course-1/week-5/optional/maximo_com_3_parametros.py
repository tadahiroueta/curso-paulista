def maximo(x,y,z):
    if x>y:
        if x>z:
            return x
        return z
    if y>z:
        return y
    return z
