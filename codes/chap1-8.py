# Function to implement Stein's Algorithm
# Input: positive integers a and b, with a > b .
# Output: the greatest common divisor of a and b.
def binary_gcd(a, b):
# Finding 'k', which is the greatest power of 2
# that divides both 'a' and 'b'.
    k = 0
    while(((a | b) & 1) == 0) :
        a = a >> 1
        b = b >> 1
        k = k + 1
# Dividing 'a' by 2 until 'a' becomes odd
    while ((a & 1) == 0) :
        a = a >> 1
# From here on, 'a' is always odd.
    while(b != 0) :
# If 'b' is even, remove all factor of 2 in 'b'
        while ((b & 1) == 0) :
            b = b >> 1
# Now 'a' and 'b' are both odd.
#Swap if necessary so a <= b
        if (a > b) :
            a, b = b, a  # Swap 'a' and 'b'.
        b = (b - a)      # b = b - a (which is even).
# restore common factors of 2
    return (a << k)