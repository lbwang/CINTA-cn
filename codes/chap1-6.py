def divide(a, b):
    if(a == 0):
        return 0, 0
    q, r = divide(a // 2, b)
    q, r = 2 * q, 2 * r
    if(a & 1): #if a is an odd number
        r = r + 1
    if(r >= b):
        r, q = r - b, q + 1
    return q, r