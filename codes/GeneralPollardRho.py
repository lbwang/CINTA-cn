def PollardRho(N):
    x1 = x2 = randint(1, N)
    while True:
        x1 = F(x1, N)
        x2 = F(F(x2, N), N)
        p = gcd(x1 - x2, N)
        if p != 1 and p != N:
            return p
