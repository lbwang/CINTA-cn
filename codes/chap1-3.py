# Input: two integers a and b, where a >= b.
# Output: the product of a and b.
def naive_multiply(a, b):
  if b == 0:
    return 0
  return  a + naive_multiply(a, b - 1)
