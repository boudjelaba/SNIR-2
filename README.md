# SNIR-2

---

##

```cpp
#include <stdio.h>

void afficher(int *num)
{
    printf("%d \t", *num);
}

int main()
{
     int tab[2][5] = {{0, 1, 2, 3, 4},{5, 6, 7, 8, 9}};
     for (int i=0; i<2; i++)
     {
        for (int j=0; j<5; j++)
        {
            afficher(&tab[i][j]);
        }
        printf("\n");
     }
     return 0;
}

---

## Permutation :

```cpp
#include <stdio.h>

void perm(int a, int b, int *an, int *bn)
{
    *an = b;
    *bn = a;
}

int main()
{
    int a=5, b=10, an, bn;
    printf("Avant permutation : a = %d et b = %d \n", a,b);
    perm(a,b,&an,&bn);

    printf("Après permutation : a = %d et b = %d \n", an,bn);
    return 0;
}
```
---

```cpp
#include <stdio.h>

int main()
{
    int i = 5, N = 3;
    double a, b, c, d;
    a = i/N;
    b = 5.0/N;
    c = ((double)(i/N));
    printf("a =  %f\n", a);
    printf("b =  %f\n", b);
    printf("c =  %f\n", b);
    return 0;
}
