# a script to check if Zn* is not a cyclic group.
p = 5
q = 3
n = p * q

# Const Zn*
#Input n
#Output: Zn* and its size
def cons_Zn(n):
    Zn = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            Zn += [i]
    #print("The size of Zn is", len(Zn))
    return Zn, len(Zn)

def check(Zn):
    for x in Zn:
        temp = []
        for i in range(len(Zn)):
            a = x**i % n
            if not (a in temp):
                temp += [a]
        if temp  == Zn:
            print("Zn is a cyclic group.")
            return True
    print("Zn is not a cyclic group.")
    return False

#Input: n
#Output: a homomorphism of Z --> <g>, and the generator
def cons_homo(n):
    Zn, size = cons_Zn(n)
    idx = randint(1, size)
    homo = [1]
    gen = Zn[idx]
    g = gen
    while not (g in homo):
        homo += [g]
        g = g*gen % n
    return homo, gen

Zn, size = cons_Zn(n)
hom, gen = cons_homo(n)