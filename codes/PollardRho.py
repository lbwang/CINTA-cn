def PollardRho(N):
    i, k = 1, 2
    x = randint(0, N - 1)
    y = x
    while True:
        i = i + 1
        x = ((x^2) - 1) % N
        divisor = gcd(y - x, N)
        if divisor != 1 and divisor != N:
            return divisor
        if i == k:
            y, k = x, 2*k