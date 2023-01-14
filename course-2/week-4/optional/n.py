import random

def lista_grande(n):
    lis = []
    for i in range(n): lis.append(random.randint(1, 1000))
    return lis
