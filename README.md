# SNIR-2

---

## Code::Blocks

https://www.youtube.com/watch?v=cHGIIp3rGO8

---

```cpp
#include <stdio.h>
int main()
{
    char TXT[201]; 
    int I, J;

    printf("Entrez une ligne de texte (max.200 caractères) :\n");
    gets(TXT);

    for (J = 0, I = 0; TXT[I]; I++)
    {
        TXT[J] = TXT[I];
        if (TXT[I] != 'e')
            J++;
    }
    /* Terminer la chaîne */
    TXT[J] = '\0';
    puts(TXT);
    return 0;
}
