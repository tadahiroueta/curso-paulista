def primeiro_lex(lista):
    outString = 'チ'

    for str in lista:
        if str < outString:
            outString = str

    return outString
