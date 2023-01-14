def imprime_matriz(Matrx):

    for i in Matrx:

        for ii in i:

            if not ii == i[-1]:
                print(ii,end=' ')

            else:
                print(ii)
