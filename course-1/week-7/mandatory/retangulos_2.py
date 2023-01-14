l=int(input('digite a largura: '))
a=int(input('digite a altura: '))
if a>0 and l>0:
    for i in range(l):
        print('#',end='')
    print()
    for i in range(a-2):
        print('#',end=' '*(l-2))
        print('#')
    if a>1 and l>1:
        for i in range(l):
            print('#',end='')
        
