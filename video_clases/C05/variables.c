#include <stdio.h>
#include <cs50.h>

// funcion principal
int main()
{
    /*
        tipos de datos
        int, float, double, long, char, string, bool.

        Varible: es un contenedor de un dato.

        declarar o crear variables

        Tipo_Dato + nombre + iniciliazcion
    */

    // crear variables
    int numero;
    float real;
    double doble;
    char letra;
    string cadena;
    bool bandera;

    // Inicializar
    numero = 10;
    real = 10.5;
    doble = 100.58;
    letra = 'a';
    cadena = "michael";
    bandera = true;

    /* especificadores de formato */
    /*
        %i,%d = int
        %li = long
        %f = float, doubles
        %c = char
        %s = strings
    */
    printf("------------------------------------\n");
    // Mandar a imprimir esos valores
    printf("numero: %i \n", numero);
    printf("real: %f \n", real);
    printf("doble: %f \n", doble);
    printf("letra: %c \n", letra);
    printf("cadena: %s \n", cadena);

    // ¿como podria capturar o recibir una informacion o pedirla?
    /*
         cs50
         "gets"
         get_int()
         get_char()
         get_string()
         get_float()
         get_double()
         get_long()
    */
    printf("------------------------------------\n");
    // actualizar los valores
    numero = get_int("Nuevo numero: ");
    real = get_float("Nuevo real: ");
    doble = get_double("Nuevo doble: ");
    letra = get_char("Nueva letra: ");
    cadena = get_string("Nueva cadena: ");

    printf("------------------------------------\n");
    // Mandar a imprimir esos valores
    printf("Nuevo numero: %i \n", numero);
    printf("Nuevo real: %f \n", real);
    printf("Nuevo doble: %f \n", doble);
    printf("Nuevo letra: %c \n", letra);
    printf("Nuevo cadena: %s \n", cadena);
}