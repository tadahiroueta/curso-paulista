def encontra_impares(li):
    if len(li) == 0: return []

    if li[-1] % 2 == 0: return encontra_impares(li[:-1])

    return encontra_impares(li[:-1]) + [li[-1]]
