def product1(X):
    res = 1
    for i in range(len(X)):
        res *= X[i]
    return res