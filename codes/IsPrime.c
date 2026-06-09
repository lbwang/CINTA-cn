/* This is a compact version. */
int IsPrime(int n, int k) 
{ 
    /* Find q such that n = 2^r * q + 1 for some r >= 1 */
    int q = n - 1; 
    while (q % 2 == 0)  q /= 2; 
    /* Iterate k times */
    for (int i = 0; i < k; i++) 
         if (!MillerRabinTest(q, n)) 
              return 0; 
    return 1; 
} 
