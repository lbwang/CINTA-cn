# lbwang 20190823
def legendre_symbol(a, p):
    if pow(a,(p-1)/2, p) == 1:
        return 1
    else:
        return -1