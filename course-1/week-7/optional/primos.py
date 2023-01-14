def n_primos(n):
    x=0
    while n>1:
        y=2
        z=0
        while y<=n/2 and z==0:
            if n%y==0:
                z=1
            y+=1
        if z==0:
            x+=1
        n-=1
    return x
