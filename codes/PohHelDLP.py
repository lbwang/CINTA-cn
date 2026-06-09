#Problem: Given base g, y \in <g>, y = g^x mod p, to find x.
def Pohlig_Hellman(y, g, p):
    prime_list = factor(p - 1)
    n = len(prime_list)
    q_list = [prime_list[i][0]^prime_list[i][1] for i in range(n)]
    G = [ g^((p - 1) // q_list[i]) for i in range(n) ] 
    Y = [ y^((p - 1) // q_list[i]) for i in range(n) ] 
    val_list = [discrete_log(Y[i], G[i]) for i in range(n)]
    modulus_list = [q_list[i] for i in range(n)] 
    x = crt(val_list, modulus_list)  # solve the CRT problem.
    return x
