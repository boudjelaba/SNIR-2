# SNIR-2

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
