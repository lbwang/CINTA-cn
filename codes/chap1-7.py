# Input: positive integers a and b, with a > b .
# Output: the greatest common divisor of a and b.
def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)
