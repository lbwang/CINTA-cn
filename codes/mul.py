# Simple mul
# Input unsigned integers a and b
# Output a * b
def multiply(a, b):
    result = 0
    #teminate when b == 0 
    while (b != 0):
        # b is even or odd
        if (b % 2):
            result += a
        # b / 2
        b = b >> 1
        # a *= 2
        a = a << 1
    return result
