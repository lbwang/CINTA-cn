# Input: integers a and b, with a > b .
# Output: d=gcd(a,b), and
# r and s s.t. d = a*r + b*s
def egcd(a, b):
    r0, r1, s0, s1 = 1, 0, 0, 1
    while(b):
        q, a, b = a//b, b, a%b
        r0, r1 = r1, r0 - q*r1
        s0, s1 = s1, s0 - q*s1
    return a, r0, s0