#Input: 多项式f和g
#Output: f和g的最大公因子
def poly_gcd(f, g):
    while g != 0:
        r = f % g  #求f除g得到的余数
        f = g
        g = r
    return f