#Input: a, b, n
#Output: x, s.t. ax \equiv b (mod n)
def modular_linear_equation_Solver(a, b, n):
    res = []
    (d, x, y) = xgcd(a, n) #egcd in Sage.
    if d.divides(b):
        x0 = (x*(b//d)) % n
        for i in range(d): #i from 0 to d - 1
            res = res + [(x0 + i*(n//d)) % n]
    else:
        print("no solutions...")
    return res
