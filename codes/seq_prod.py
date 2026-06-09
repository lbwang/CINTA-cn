# Input: Given a sequence of number X
# Output: The product of all the numbers in X
def product1(X):
    res = 1
    for i in range(len(X)):
        res *= X[i]
    return res

# Input: Given a sequence of number X
# Output: The product of all the numbers in X
def product2(X):
    l = len(X)
    if l == 0: return 1
    if l == 1: return X[0]
    if l == 2: return X[0]*X[1]
    return product2(X[0:(l+1)//2]) * product2(X[(l+1)//2: l])
    
# Input: Given a sequence of number X
# Output: The product of all the numbers in X
def product(X):
    if len(X) == 0: return 1
    while len(X) > 1:
        #prod is a build-in function of Sage.
        X = [prod(X[i*2:(i+1)*2]) for i in range((len(X)+1)/2)] 
    return X[0]
