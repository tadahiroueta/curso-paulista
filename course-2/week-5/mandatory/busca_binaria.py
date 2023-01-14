def busca(lista, elemento):
    st = 0
    last = len(lista) - 1

    while st <= last:
        mid = (st + last) // 2
        print(mid)
        midV = lista[mid]

        if midV == elemento: return mid

        elif midV > elemento: last = mid - 1

        else: st = mid + 1

    return False
