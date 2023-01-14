def ordenada(lista):
    for n in range(len(lista)):
        if n != 0:
            if lista[n - 1] > lista[n]:
                return False

    return True
