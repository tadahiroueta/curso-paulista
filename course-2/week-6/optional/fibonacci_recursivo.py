def fibonacci(n, a = 0, aa = 1):
    if n == 1: return aa

    a, aa = aa, a + aa
    return fibonacci(n - 1, a, aa)
