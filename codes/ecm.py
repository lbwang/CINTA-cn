def ecm(N, B=10^3, trials=10):
    m, R= lcm(1,2,...,B), Integers(N)
    R.is_field = lambda : True #Make Sage think that R is a field.
    for _ in range(trials):
        a = ChooseRandomA()
        try:
            m * EllipticCurve([a, 1])([0,1])
        except ZeroDivisionError as msg:
            # msg: "Inverse of <int> does not exist"
            return gcd(Integer(str(msg).split()[2]), N)
    return 1