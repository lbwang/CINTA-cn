# Input: g,y,n，其中g是群的基底，y = g^x, p是g的阶.
def BSGS(g, y, p):
    s = floor(sqrt(p))
    A = [(y*(g^r) % p) for r in range(0, s)]   #Baby Step.
    B = [(g^(t*s) % p) for t in range(1, s+1)] #Giant Step.
    r,t = 0,0
    for u in A:
        for v in B:
            if u == v:  #Collision.
                r, t = A.index(u), B.index(v)
    return ((t+1)*s - r) % p  # Return x