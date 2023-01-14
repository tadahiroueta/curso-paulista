def incomodam(n):
    if n < 0 or not isinstance(n, int): return ''

    return 'incomodam ' * n

def elefantes(n):
    if n <= 1 or not isinstance(n, int): return ''

    if n == 2:
        return 'Um elefante incomoda muita gente\n2 elefantes %smuito mais' % incomodam(n)

    return elefantes(n - 1) + '\n%i elefantes incomodam muita gente\n%i elefantes %smuito mais' % (n - 1, n, incomodam(n))
