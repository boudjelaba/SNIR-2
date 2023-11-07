#include <stdio.h>
#include <stdlib.h>
 
int main()
{
 
    char trame[500];
    char T[500];
 
int i,s;
 
 
s=0;
    do
    {
 
 
    printf("Entrer la trame:     ");
     gets(trame);
 
     if (strlen(trame)< 144)
        {
        printf("\nVeuillez saisir une trame valide!\n\n");
        }
else
{
 
 
        for (i=0; i<strlen(trame); i++)
 
{
    T[i]=trame[i];
}
 
for (i=44; i<=strlen(trame)-9; i++)
{
    s=s+1;
}
 
 
if (s<92)
{
     printf(" Le data ip de cette trame n'est pas valide    ");
}
 
}
    }
 
 
while (strlen(trame)<144);
 
 
 
 
 
for (i=0; i<strlen(trame); i++)
 
{
    T[i]=trame[i];
}
printf("\n------------------------------------------------------------------------------------------- ");
printf("\nLe Preambule de cette trame est:  ");
 
for (i=0; i<=13; i++)
{
    printf("%c",T[i]);
}
printf("\n------------------------------------------------------------------------------------------- ");
 
printf("\nLe SFD de cette trame est:    ");
 
for (i=14; i<=15; i++)
{
    printf("%c",T[i]);
}
printf("\n------------------------------------------------------------------------------------------- ");
 
printf("\nL'Adresse MAC Destination de cette trame est: ");
 
 
for (i=16; i<=27; i++)
{
    printf("%c",T[i]);
}
printf("\n------------------------------------------------------------------------------------------- ");
 
printf("\nL'Adresse MAC Source de cette trame est:  ");
 
 
for (i=28; i<=39; i++)
{
    printf("%c",T[i]);
}
printf("\n------------------------------------------------------------------------------------------- ");
 
printf("\nLe Ether Type de cette trame est:   ");
 
for (i=40; i<=43; i++)
{
    printf("%c",T[i]);
}
 
printf("\n------------------------------------------------------------------------------------------- ");
 
 
printf("\nLe data ip de cette trame est:  ");
for (i=44; i<=strlen(trame)-9; i++)
{
    printf("%c",T[i]);
}
printf("\n------------------------------------------------------------------------------------------- ");
 
printf("\nLe FCS de cette trame est:  ");
 
for (i=strlen(trame)-8; i<=strlen(trame)-1; i++)
{
    printf("%c",T[i]);
}
printf("\n------------------------------------------------------------------------------------------- ");
 
 
 
 
 
 
s=0;
i=strlen(trame)-9;
int b=0;
int bourr=0;
 
for (i=44; i<=strlen(trame)-9; i++)
{
    s=s+1;
}
 
 
if (s==92)
    printf("\n\nLa taille de la DATA IP de cette trame est 46 Octets");
{
while ( (i>=44) && (bourr==0) )
{
 
    if ( (T[i]=='0') && (T[i-1]=='0')  )
    {
 
             b=b+1;
    }
 
    else
    {
        bourr=1;
    }
 
 
           i=i-2;
 
}
 
 
if (b!=0)
{
printf(" et elle contient %d Octet(s) de bourrage\n\n",b);
}
 else if ((s==92) && (b==0))
 {
printf(" mais elle ne contient pas des Octets de bourrage\n\n");
 
 }
}
 
 
/*
Ex de trame valide
000573a00000e06995d85a1386dd60000000009b06402607530000602abc00000000badec0de200141d000024233000000000000000496740050bcea7db800c1d703801800e1cfa000000101080a093e69b917a17ed3474554202f20485454502f312e310d0a417574686f72697a6174696f6e3a20426173696320593239755a6d6b365a47567564476c6862413d3d0d0a557365722d4167656e743a20496e73616e6542726f777365720d0a486f73743a207777772e6d79697076362e6f72670d0a4163636570743a202a2f2a0d0a0d0a
Ex de trame avec bourrage
000573a00000e06995d85a1386dd60000000009b064023616e6542726f777365720d0a486f73743a207777772e6d79697076362e6f72670d0a4163636570743a000000000d0a0d0a
Ex de trame sans bourrage
000573a00000e06995d85a1386dd60000000009b064023616e6542726f777365720d0a486f73743a207777772e6d79697076362e6f72670d0a4163636570743abdhehdgs0d0a0d0a
*/
 
 
 
 
 
    return 0;
}