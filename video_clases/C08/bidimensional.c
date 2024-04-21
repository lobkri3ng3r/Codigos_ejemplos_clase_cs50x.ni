#include <stdio.h>
#include <cs50.h>

void recorrer_bidi(int matriz[3][3]);

// Funcion main
int main()
{
    // Instrucciones

    /*
        arreglo bidimensional -----> matriz ------> filas * columnas
    */

    // Tipo_dato + nombre + dimension
    // int filas = 3;
    // int columnas = 3;
    int matriz[3][3] = {{10,11,12},{20,21,22},{30,31,32}};

    // for (int i = 0; i < filas; i++)
    // {
    //     for (int j = 0; j < columnas; j++)
    //     {
    //         matriz[i][j] = get_int("matriz[%i][%i]: ",i,j);
    //     }
    // }

    recorrer_bidi(matriz);

}

void recorrer_bidi(int matriz[3][3])
{
    // i = filas ^ j = columnas

    printf("------------------------------------------------------------\n");

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("matriz[%i][%i] -----> %i \n",i,j,matriz[i][j] );
        }
        printf("*********************\n");
    }
}