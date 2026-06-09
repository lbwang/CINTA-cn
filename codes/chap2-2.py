# Input: integer n;
# Output: i*j mod n, with 1 <= i, j <= n - 1
def mul_mod_n(n):
  for i in range(1, n):
    for j in range(1, n):
      print i*j % n,  # i*j modulo n
    print
  return
