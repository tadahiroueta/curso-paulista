def é_hipotenusa(h):
    x=3
    y=4
    while y<25:
        while x<25:
            if(x**2+y**2)==h**2:
                return True
            x+=1
        x=1
        y+=1
    return False

def soma_hipotenusas(n):
    s=0
    while n>0:
        if é_hipotenusa(n):
            s+=n
        n-=1
    return s
