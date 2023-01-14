while True:
    n=int(input())
    x=2
    while n%x!=0 and x<n//2:
        x+=1
    if(n%x!=0 or n==2)and n!=1:
        print(True)
    else:
        print(False)
