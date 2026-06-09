def PollardPM1(N, B=10^5, stop=10):
    m = prod([p^int(math.log(B)/math.log(p)) 
    for p in prime_range(B + 1)])
    # p^x, where x = ceiling(log_p B)
    for a in range(2, stop):
        x = (Mod(a,N)^m - 1).lift()
        if x == 0: continue
        divisor = gcd(x, N)
        if divisor != 1 and divisor != N: return divisor
    return 1