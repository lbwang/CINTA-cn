###############################
##Sample codes for CINT
##Author: Libin Wang
##Date: 2018.05.18
###############################
def divide(a, b):
    q, r = 0, 0
    while(a >= b):
        a, q = a - b, q + 1
    r = a
    return q, r

def rec_divide(a, b):
    if(a == 0):
        return 0, 0
    q, r = rec_divide(a // 2, b)
    q, r = 2 * q, 2 * r
    if(a & 1): #if a is an odd number
        r = r + 1
    if(r >= b):
        r, q = r - b, q + 1
    return q, r

# Function to implement Euclidean's Algorithm
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

# Function to implement Stein's
# Algorithm
def binary_gcd( a, b) :

    # GCD(0, b) == b; GCD(a, 0) == a,
    # GCD(0, 0) == 0
    if (a == 0) :
        return b

    if (b == 0) :
        return a

    # Finding K, where K is the greatest
    # power of 2 that divides both a and b.
    k = 0

    while(((a | b) & 1) == 0) :
        a = a >> 1
        b = b >> 1
        k = k + 1

    # Dividing a by 2 until a becomes odd
    while ((a & 1) == 0) :
        a = a >> 1

    # From here on, 'a' is always odd.
    while(b != 0) :

        # If b is even, remove all factor of
        # 2 in b
        while ((b & 1) == 0) :
            b = b >> 1

        # Now a and b are both odd. Swap if
        # necessary so a <= b, then set
        # b = b - a (which is even).
        if (a > b) :

            # Swap u and v.
            a, b = b, a

        b = (b - a)

    # restore common factors of 2
    return (a << k)

    def egcd(a, b):
	    x0, x1, y0, y1 = 1, 0, 0, 1
	    while(b):
	        q, a, b = a//b, b, a%b
	        x0, x1 = x1, x0 - q * x1
	        y0, y1 = y1, y0 - q*y1
	    return a, x0, y0
