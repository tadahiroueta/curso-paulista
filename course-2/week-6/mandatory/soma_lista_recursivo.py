def soma_lista(lista, n = 0):
    if n == len(lista): return 0

    return lista[n] + soma_lista(lista, n + 1)
