i=int(input('Digite um número inteiro: '))
d=0
a=10
c=False
while 10**d<i:
    b=(i//(10**d))%10
    if a==b:
        c=True
        break
    a=b
    d+=1
if c==True:
    print('sim')
else:
    print('não')
