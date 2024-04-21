#include <stdio.h>
#include <cs50.h>

int longitud(string cadena);

// Funcion main
int main()
{
    string texto = get_string("Texto: ");
    int longitud_texto = longitud(texto);
    printf("longitud del texto: %i\n",longitud_texto);

    for(int i = 0; i < longitud_texto; i++)
    {


        texto[i] += 1;
        // // printf("%c\n",texto[i]);
        // if(texto[i] == 'a')
        // {
        //     texto[i] = '@';
        // }
        // else if(texto[i] == 'e')
        // {
        //     texto[i] = '3';
        // }
        // else if(texto[i] == 'i')
        // {
        //     texto[i] = '!';
        // }
        // else if(texto[i] == 'o')
        // {
        //     texto[i] = '0';
        // }
        // else if(texto[i] == 'u')
        // {
        //     texto[i] = 'n';
        // }
    }

    printf("%s \n",texto);

}

int longitud(string cadena)
{
    int cant_palabras = 0;

    while(cadena[cant_palabras] != '\0')
    {
        cant_palabras ++;
    }

    return cant_palabras;

}