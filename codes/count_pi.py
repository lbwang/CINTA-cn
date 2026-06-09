# compute pi(x)
def count_pi(n):
   i = 3
   sum1 = 0
   sum2 = 0
   while i <= n :
       if is_prime(i):
           if (i % 4) == 1:
               sum1 += 1
           else:
               sum2 += 1
       i += 1
   return sum1, sum2