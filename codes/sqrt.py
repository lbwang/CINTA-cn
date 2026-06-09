#take from WStein-ENT
#edited by lbwang, but i don't know much about it.
def find_sqrt(a, p):
    assert (p-1)%4 == 0
    assert legendre_symbol(a,p) == 1
    S.<x> = PolynomialRing(GF(p))
    R.<alpha> = S.quotient(x^2 - a)
    while True:
        z = GF(p).random_element()
        w = (1 + z*alpha)^((p-1)//2)
        (u, v) = (w[0], w[1])
        if v != 0: break
    if (-u/v)^2 == a: return -u/v
    if ((1-u)/v)^2 == a: return (1-u)/v
    if ((-1-u)/v)^2 == a: return (-1-u)/v