#Input: y = g^x mod p; Output: x
def PollardRhoDLOG(y):
    left, lg, ly = 1, 0, 0  # left = g^lg * y^ly
    right, rg, ry = y, 0, 1 # right = g^rg * y^ry
    while left != right:
        left, lg, ly = F(left, lg, ly)
        right, rg, ry = F(right, rg, ry)
        right, rg, ry = F(right, rg, ry)
    s, t = lg - rg, ry - ly
    if s == 0:
        return 'fail'
    return s * (t^(-1))

