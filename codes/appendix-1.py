# Function for nth fibonacci number
def fibonacci(n):
    if (n == 0):
      return 0
    if (n == 1):
      return 1
    a, b = 0, 1
    for i in range(1,n):
      c = a + b
      a = b
      b = c
    return b
