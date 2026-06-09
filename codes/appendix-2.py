n = 17
for i in range(3, n):
  print "F%u / F%u = %.9f" %(i, i-1, float(fibonacci(i)) / float(fibonacci(i-1)))
  print
