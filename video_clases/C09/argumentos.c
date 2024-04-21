#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    /*
    argc ---> cantidad de argumentos
    argv ----> el valor de los argumentos
    ??????? que wea es un argumento???
    */
   printf("cantida de argumentos: %i \n",argc);

   if (argc != 2)
   {
    printf("Error demasiado o muy pocos argumentos \n");
    return 1;
   }

    int n = strlen(argv[1]);

    for (int i = 0; i < n ; i++)
    {
        if(isdigit(argv[1][i]))
        {
            printf("Es un digito \n");
        }
        else{
            printf("Error clave invalida \n");
            return 2;
        }
        // printf("argumento[1][%i] ---> %c \n",i,argv[1][i]);
    }

}