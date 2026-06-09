# Input: n是一个标量，P是椭圆曲线上的一个点
# Output: nP，即n个P的点加
def DoubleAdd(n, P):
    R = 0
    Q = P
    while(n > 0 ):
        if is_odd(n):
            R = R + Q
        Q = 2 * Q 
        n = n // 2
    return R