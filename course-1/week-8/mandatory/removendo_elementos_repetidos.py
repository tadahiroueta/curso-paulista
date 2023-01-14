def remove_repetidos(x):
    b=None
    c=0
    d=0
    l=sorted(x[:])
    for i in x:
        a=b
        b=l[c-d]
        if a==b:
            del l[c-d]
            d+=1
        c+=1
    return l
