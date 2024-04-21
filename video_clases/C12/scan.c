#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h> // Aqui se encuentra la funcion malloc

int main()
{
    int numero;
    scanf("%i",&numero);
    printf("numero: %i\n",numero);

    char *s = malloc(5);
    scanf("%s",s);
    printf("cadena: %s\n",s);

}

