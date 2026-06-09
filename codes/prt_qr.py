p = 11
a = 5
def print_qr(p):
    for i in range(1, p):
        print i,
    print
    for i in range(1, p):
        print pow(i,2) % p,
    print

# cubic residue.
# when p = 2 mod 2, the output is a perm of Zp^*
def print_cr(p):
    for i in range(1, p):
        print i,
    print
    for i in range(1, p):
        print pow(i,3) % p,
    print
