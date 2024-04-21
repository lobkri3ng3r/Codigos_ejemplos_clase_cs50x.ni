#include <stdio.h>
#include <cs50.h>

void mario(int n); // Prototipo funcion de mario

int main()
{
    int altura = get_int("Altura: ");
    mario(altura); // LLAMAR A FUNCION MARIO DESDE MAIN
}

void mario(int n) // Definicion funcion mario
{
    // Caso Base
    if (n <= 0){
        return;
    }

    mario(n-1); // LLAMAMOS NUESTRA FUNCION RECURSIVA

    for(int i = 0; i < n; i++)
    {
        printf("#");
    }
    printf("\n");


}