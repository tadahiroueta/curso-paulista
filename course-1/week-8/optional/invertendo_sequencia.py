l=[]
x=None
while x!=0:
    if x!=None:
        l.append(x)
    x=int(input('Digite um número: '))
print()
for i in range(len(l)):
    x-=1
    print(l[x])
