#Paillier Enc Scheme
#20180621
#Author: Libin Wang
def KG(n):
    while(1):
        p = random_prime(10^(n-1), 10^n)
        if p.is_prime():
            break
    while(1):
        q = random_prime(10^(n-1), 10^n)
        if (p != q) and q.is_prime() and (q.ndigits() == p.ndigits()):
            break
    N = p*q
    phi_N = (p - 1)*(q - 1)
    return (N, phi_N)

def Sample_ZN(N):
    while(1):
        r = Integer(randrange(N))
        if gcd(r, N) == 1:
            break
    return r
#Input: m \in Z_N and N
#Output: Cipher Text
def Enc(m, N):
    N2 = N * N
    r = Sample_ZN(N)
    c1 = pow((1 + N), m, N2)
    c2 = pow(r, N, N2)
    c = Mod(c1, N2) * Mod(c2, N2)
    return c

def Dec(c, N, phi_N):
    N2 = N * N
    c1 = pow(c, phi_N, N)
    m1 = (c1 - 1) // N
    m = Mod(m1, N) * Mod(phi_N^(-1), N)
    return m
