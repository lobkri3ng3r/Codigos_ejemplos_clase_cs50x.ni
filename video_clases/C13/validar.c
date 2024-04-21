#include <stdio.h>
#include <cs50.h>

int main()
{
    // FILE ---> ESPERA UN PUNTERO
    FILE *archivo = fopen("nombres.txt", "r");

    // Comprobar si se abre correctamente
    if (archivo == NULL)
    {
        printf("Error al abrir el archivo \n");
        return 1;
    }

    char caracter;
    int n = 0; // cantidad de ? letras

    //EOF indica el final de un archivo
    while((caracter = fgetc(archivo)) != EOF)
    {
        if(caracter == 'a' || caracter == 'A')
        {
            n++;
        }
    }

    // Cantidad de letras a que hay en el archivo
    printf("La cantidad de letras a | A es: %i\n",n);

    // cerrar el achivo
    fclose(archivo);
}