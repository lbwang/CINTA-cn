# Input: positive integers a and b, with a > b .
# Output: the greatest common divisor of a and b and Bezout coefficients.
def binary_egcd(a, b):
# Finding 'k', which is the greatest power of 2 that divides both 'a' and 'b'.
    k = 0
    while(((a | b) & 1) == 0):
        a >>= 1
        b >>= 1
        k += 1
    r0, r1 = a, b
    s0, s1, t0, t1 = 1, 0, 0, 1
    while(r1 != 0):
        #If r0 is even, remove all factor of 2 in r0
        while ((r0 & 1) == 0):
            r0 >>= 1
            if (((s0 | t0) & 1) == 0):
                s0 >>= 1
                t0 >>= 1
            else:
                s0 = (s0 + b) >> 1
                t0 = (t0 - a) >> 1
        #If r1 is even, remove all factor of 2 in r1
        while ((r1 & 1) == 0) :
            r1 >>= 1
            if (((s1 | t1) & 1) == 0):
                s1 >>= 1
                t1 >>= 1
            else:
                s1 = (s1 + b) >> 1
                t1 = (t1 - a) >> 1
        if (r1 < r0):
            r0, s0, t0, r1, s1, t1 = r1, s1, t1, r0, s0, t0
        r1 = r1 - r0
        s1 = s1 - s0
        t1 = t1 - t0
    r0 <<= k
    return r0, s0, t0