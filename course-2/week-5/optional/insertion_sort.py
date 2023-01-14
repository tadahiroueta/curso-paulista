def insertion_sort(lista):
    for i in range(1, len(lista)):
        mov = lista[i]
        
        for j in range(i - 1, -1, -1):
            
            if mov < lista[j]: lista[j], lista[j + 1] = mov, lista[j]

    return lista
