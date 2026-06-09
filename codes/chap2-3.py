# Recursive Function to calculate
# (x^y)%p in O(log y)
def rec_mod_exp(x, y, p):
    if (y == 0): return 1
    z = rec_mod_exp(x, y//2, p)
    if ((y & 1) == 0): #y is an even number
        return z*z % p
    else:              #y is an odd number
        return x*z*z %p
