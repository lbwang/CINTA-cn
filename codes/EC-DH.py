p = next_prime(randrange(10^40))
F = FiniteField(p)
E = EllipticCurve(F, [F.random_element(), F.random_element()])
P = E.random_element()
b = randrange(1000); b
B = b*P
a = randrange(1000); a
A = a*P
if(a*B == b*A): print "We share a common secret."