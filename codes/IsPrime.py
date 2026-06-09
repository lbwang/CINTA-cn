#Input: 整数n和米勒测试的次数
#Output: 如果n通过k次米勒测试，输出1，否则输出0
def IsPrime(n, k):
    q = n - 1
    while is_even(p):
        q /= 2
    for i in range(k):
        a = randint(2, n - 1)
        if not MillerTest(a, q, n):
            return 0
    return 1
    
  