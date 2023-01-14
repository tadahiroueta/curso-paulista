def ordena(lista):
    for n in range(len(lista)):
        for n2 in range(len(lista)):
            if lista[n] > lista[n2] and n < n2:
                lista[n], lista[n2] = lista[n2], lista[n]

    return lista
