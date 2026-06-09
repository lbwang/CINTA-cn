#Input: a是随机选取的基，n是要测试的整数，而q是整数满足n-1 = 2^k q
#Output: 如果n是合数，输出0；否则n可能是素数，输出1，即通过米勒测试;
def MillerTest(a, q, n):
    x = pow(a, q, n)
    if (x == 1) or (x == (n - 1)):  
        return 1
    while q != (n - 1):
        x = (x * x) % n
        q *= 2
        if x == (n - 1): 
            return 1
    return 0
