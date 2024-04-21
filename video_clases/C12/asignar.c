#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h> // Aqui se encuentra la funcion malloc

int main()
{
    char *s1 = get_string("s1: ");
    char *s2 = malloc(strlen(s1) + 1); // Asignar memoria de manera dinamica con malloc

    if (s2 == NULL) // Comprobar si se asigno correctamente memoria
    {
        printf("Algo salio mal, no se pudo asignar memoria \n");
        return 1;
    }

    int n = strlen(s1); // guardar la longitud de la cadena

    // copiar lo de s1 a s2
    strcpy(s2,s1);
    // for(int i = 0; i < n; i++)
    // {
    //     s2[i] = s1[i];
    // }

    printf("---------------\n");
    printf("S1: %s\n",s1);
    printf("S2: %s\n",s2);

    // Liberar memoria
    free(s2);

    return 0;

}

