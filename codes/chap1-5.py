def naive_divide(a, b):
    q, r = 0, 0
    while(a >= b):
        a, q = a - b, q + 1
    r = a
    return q, r