#多项式除法
#Input: f和g(g != 0)，两个不定元为x的域上多项式;
#Output: q(商),r(余数);
def poly_div(f, g):
    q = 0
    r = f
    d = deg(g) #g的阶
    c = lc(g)  #lc返回g的首项系数
    while deg(r) >= d:
        temp_c = lc(r) / c  #注意，此为域的除法
        temp_pow = deg(r) - d
        s = temp_c*x^temp_pow  #构成多项式的某一阶的项
        q = q + s    #多项式加法
        r = r - s*g  #多项式减法
    return (q, r)
