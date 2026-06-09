## Play with EC using Sage.
# The elliptic curve y^2 = x^3 - 5x + 4 over R.
E0 = EllipticCurve(RR, [-5, 4])
show(plot(E0, hue=.9))
# The elliptic curve over F_p.
p = 137
F = FiniteField(p)
E1 = EllipticCurve(F, [F.random_element(), F.random_element()])
print E1
E1.points()
show(plot(E1, hue=.9))
