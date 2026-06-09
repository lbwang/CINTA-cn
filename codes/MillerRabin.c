/* Compact version to be show in Beamer.*/
int MillerRabinTest(int q, int n) 
{ 
    int a = 2 + rand() % (n - 4); /*Pick a random number.*/
    int x = power(a, q, n); /* Compute a^q % n */
    if (x == 1  || x == n-1)  return 1; 
    while (q != n-1) 
    { 
        x = (x * x) % n; 
        q *= 2; 
        if (x == n-1)  return 1; 
    } 
    return 0; 
} 