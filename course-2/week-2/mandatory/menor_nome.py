def menor_nome(nomes):
    outNome = '                   '

    for nome in nomes:
        if len(outNome) > len(nome.strip()):
            outNome = nome.strip().capitalize()

    return outNome
