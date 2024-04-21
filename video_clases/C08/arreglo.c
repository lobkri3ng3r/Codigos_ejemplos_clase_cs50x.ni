// Librerias
#include <stdio.h>
#include <cs50.h>

// Funcion main
int main()
{
    // Instrucciones
    /*
        arreglo = estructra de datos que guarda elementos de un mismo tipo de datos cuyos valores estan de manera
        consecutiva. [1,2,3,4,5,6]
    */

    // Tipo dato + nombre + dimension
    int numeros[] = {10,20,30,40,50,60};
    // Los indices incian e 0 Y terminan en N-1;
    // [0,1,2,3,4]

    // for(int i = 0; i < 5; i++)
    // {
    //     numeros[i] = get_int("dame un numero: ");
    // }

    for(int i = 0; i < 6; i++)
    {
        printf("numeros[%i] -----> %i\n",i,numeros[i]);
    }


    //    numeros[0] = 10;
    //    numeros[1] = 20;
    //    numeros[2] = 30;
    //    numeros[3] = 40;
    //    numeros[4] = 50;

    //    printf("%i\n",numeros[0]);
    //    printf("%i\n",numeros[1]);
    //    printf("%i\n",numeros[2]);
    //    printf("%i\n",numeros[3]);
    //    printf("%i\n",numeros[4]);
}