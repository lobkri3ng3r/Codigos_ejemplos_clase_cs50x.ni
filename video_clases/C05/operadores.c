// librerias
#include <stdio.h>
#include <cs50.h>

// funcion main
int main()
{
    /*operadores aritmeticos*/
    /* + - * / % */
    /*
        10%2 = 0
    */

    // declaracion e inicilizacion
    int numero1 = get_int("numero 1: ");
    int numero2 = get_int("numero 2: ");

    // Operacion aritmeticas
    int suma = numero1 + numero2;
    int resta = numero1 - numero2;
    int multi = numero1 * numero2;
    int div = numero1 / numero2;
    int modulo = numero1 % numero2;

    printf("----------------------\n");
    printf("suma: %i \n", numero1+numero2);
    printf("resta: %i \n", resta);
    printf("multi: %i \n", multi);
    printf("div: %i \n", div);
    printf("modulo: %i \n", modulo);

    /* Azucar sintactica */
    int contador= 0;
    contador = contador + 1;
    contador += 1;
    contador ++;

}