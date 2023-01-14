while True:
    z=0
    print()
    n=int(input())
    x=2
    p=1
    while n!=1:
        y=n
        a=x
        while y==n:
            if n%x==0:
                n/=x
            else:
                x+=1
        if z==0:
            print(x, end='')
            a=0
        if x==a:
            p+=1
        if z==1 and x!=a:
            if p!=1:
                print('^'+str(p),end='')
                p=1
            print('*'+str(x),end='')
        z=1
    if p!=1:
        print('^'+str(p),end='')
