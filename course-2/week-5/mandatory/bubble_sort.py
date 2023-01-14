def bubble_sort(lista):
    stop = False

    while stop == False:
        stop = True

        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                print(lista)
                stop = False

    return lista
