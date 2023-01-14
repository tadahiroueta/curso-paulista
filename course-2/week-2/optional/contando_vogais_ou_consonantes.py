def conta_letras(frase, contar = 'vogais'):
    nVogais = 0
    lenFrase = 0

    for letra in frase:
        if (letra == 'a' or
            letra == 'e' or
            letra == 'i' or
            letra == 'o' or
            letra == 'u' or
            letra == 'A' or
            letra == 'E' or
            letra == 'I' or
            letra == 'O' or
            letra == 'U'):

            nVogais += 1

        if letra != ' ':
            lenFrase += 1
            
    if contar == 'vogais':
        return nVogais

    return lenFrase - nVogais
