#include <stdio.h>
#include <cs50.h>

int main()
{
    // FILE ---> ESPERA UN PUNTERO
    FILE *archivo = fopen("/workspaces/87022089/ejemplo/Hola.txt", "a");

    // Comprobar si se abre correctamente
    if (archivo == NULL)
    {
        printf("Error al abrir el archivo \n");
        return 1;
    }

    // Solicitar datos
    int cantidad = get_int("Cantidad de personas agregar: ");

    string nombre;
    string edad;

    for (int i = 0; i < cantidad; i++)
    {
        printf("----Persona #%i ------\n", i + 1);
        nombre = get_string("Nombre #: ");
        edad = get_string("Edad: ");
        // escribir sobre mi archivo
        fprintf(archivo, "Nombre: %s | Edad: %s\n", nombre, edad);
        printf("-------------------------\n");
    }

    // cerrar el achivo
    fclose(archivo);
}