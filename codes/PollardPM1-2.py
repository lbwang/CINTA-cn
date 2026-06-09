def PollardPM1(N, B=10^5):
    a = 2 # or some other value;
    for i in range(2, B):
        a = a^i % N
        divisor = gcd(a - 1, N)
        if divisor != 1 and divisor != N: 
            return divisor
    return 1