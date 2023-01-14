def maior_primo(x):
    if x==1:
        return
    while True:
        f=x//2
        while f>1:
            if x%f==0:
                f=0
            f-=1
        if f==1:
            return x
        x-=1
