#include <stdio.h>
#include <cs50.h>

void intercambio(int *x, int *y);

int main()
{
    // & direccionamiento
    int a = 10;
    int b = 20;
    intercambio(&a,&b);
    printf("a: %i\n",a);
    printf("b: %i\n",b);
}

void intercambio(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}