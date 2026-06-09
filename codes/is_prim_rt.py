# 输入素数p和一个小于p的正整数a
# 输出Ture，如果a是模p的原根，否则输出False
def is_primitive_root(a, p):
    flist = prime_fators_list(p-1) #求p-1的所有素因子
    for f in flist: 
        if pow(a, (p-1)//f, p) == 1:
            return False
    return True
