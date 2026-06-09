# Input: two integers a and b.
# Output: the product of a and b.
def multiply(a, b):
  if b == 0:
      return 0
  if is_even(b): # the last bit of b is 0;
      return 2*multiply(a, b//2)
  else: # b is odd
	    return 2*multiply(a, b//2) + a