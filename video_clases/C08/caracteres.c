#include <stdio.h>
#include <cs50.h>


// Funcion main
int main()
{
    // 1 f . ! ''
    // castear ---> convertir una variable de un tipo de dato a otro
    int c1 = (int)('H');
    int c2 = (int)('o');
    int c3 = (int)('l');
    int c4 = (int)('a');

    printf("%i %i %i %i \n",c1,c2,c3,c4);

    printf("*************************\n");

    char saludo[] = {'h','o','l','a'};
    string saludo2 = "Hola";

    printf("%s\n",saludo);
    printf("%c %c %c %c \n",saludo2[0],saludo2[1],saludo2[2],saludo2[3]);





}