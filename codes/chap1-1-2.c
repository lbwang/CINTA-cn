#include <stdio.h>
int main()
{
    unsigned char a = 255;
    printf("a + 2 == %d \n", a + 2);
    printf("a^5 == %d \n", a * a * a * a * a);
    a += 2;
    printf("a + 2 == %d \n", a);
    a = 255;
    a = a * a * a * a *a; 
    printf("a^5 == %d \n", a);
    a = 255;
    a = a * a * a * a * a *a; 
    printf("a^6 == %d \n", a);
    /* 
    int n = 32; 
    for(int i = 1; i <= n; i++)
    {
        val = val * 2;
        printf("What you get is %u \n.", val);
    }
    */
    return 0;
}
