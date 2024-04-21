#include <stdio.h>
#include <cs50.h>

/* DEFINIR NUESTRA STRUC ANTES DE LA FUNCION MAIN*/
typedef struct datos // La forma como el compilar conoce la estructura
{
    // Miembros o campos
    string nombre;
    string cedula;
    string nacionalidad;
    int telefono;
} datos; // La forma en como se utiliza o se manda a llamar la estructura

int main()
{
    datos persona[2];

    for (int i = 0; i < 2; i++)
    {
         printf("Datos persona #%i \n", i);
        persona[i].nombre = get_string("Nombre: ");
        persona[i].cedula = get_string("cedula: ");
        persona[i].nacionalidad = get_string("Nacionalidad: ");
        persona[i].telefono = get_int("telefono: ");
        printf("------------------------------------\n");
    }

    for (int i = 0; i < 2; i++)
    {
        printf("Datos persona #%i \n", i);
        printf("%s \n", persona[i].nombre);
        printf("%s \n", persona[i].cedula);
        printf("%s \n", persona[i].nacionalidad);
        printf("%i \n", persona[i].telefono);
        printf("------------------------------------\n");
    }
}