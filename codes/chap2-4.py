# Iterative Function to calculate
# (x^y)%p in O(log y)
def mod_exp(x, y, p) :
    # Initial result
    res = 1
    # view y as a binary string
    # begin with y's least significant bit
    while (y > 0) :
      # If lsb of y is 1, multiply x with result
      if ((y & 1) == 1) :
        res = (res * x) % p
      # Divide y (y = y >> 1) to get y's next bit.
      y = y // 2
      # Repeatly compute x^{2^i}, 1 < = i <= log y
      x = (x * x) % p
    return res
