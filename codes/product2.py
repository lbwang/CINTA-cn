def product2(X):
    if len(X) == 0: return 1
    if len(X) == 1: return X[0]
    if len(X) == 2: return X[0] * X[1]
    l = len(X)
    return product2(X[0:(l + 1) // 2]) * product2(X[(l + 1) // 2: l])