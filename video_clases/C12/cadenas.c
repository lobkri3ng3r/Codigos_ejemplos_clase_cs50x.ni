#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main()
{
    // Un puntero de caracteres es equivalente a un arreglo de caracteres que es equivalente a string
    // *s == S[] == string

    char *s1 = "Hi!";
    char s2[4] = "Hi!";
    string s3 = "Hi!";

    // *s1 + i == s1[i]

    printf("s: %c\n",*s1); // Desrefenciamos el puntero de caracteres para acceder a un solo caracters
    // Accedemos a un indice para mostrar un solo caracters
    printf("s: %c\n",s2[0]);
    printf("s: %c\n",s3[0]);

    printf("----------------------\n");
    // Comparacion de cadenas
    char *l1 = get_string("l1: ");
    char *l2 = get_string("l2: ");

    if (strcmp(l1,l2) == 0)
    {
        printf("son iguales \n");
    }
    else{
        printf("Son diferentes \n");
    }



}

