i=int(input('Digite um número inteiro: '))
p=1
for o in range(i//2-1):
    p+=1
    if i%p==0:
        print('não primo')
        break
if i%p!=0:
    print('primo')
