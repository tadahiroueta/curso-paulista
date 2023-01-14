def maiusculas(frases):
    output = ''

    for i in frases:

        if ord(i) > 64 and ord(i) < 91:
            output += i

    return output
