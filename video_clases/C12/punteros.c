#include <stdio.h>

int main()
{
    /*
        Es una variable que almacena direcciones de memoria
        Definicion de un puntero
        Tipo_dato + * + nombre
        1- Declarar e inicilizar
        2- Primero declarar y luego inicializar
    */
    int *p; // Crear puntero // 8 bytes // Utilizamos * para definir un puntero
    int *q;

    // referenciar que es basicamente almacenar una direccion de memoria

    int n = 50;

    p = &n; // Utilizamos amsperson o et para direccionamiento (obtiene una direccion de memoria)
    q = p;  // Cada puntero una direccion de memoria, entonces es posible compartir la informacion, asignarles el valor de otro puntero

    printf("p: %p\n", p); // %p especifica las salidas de direcciones de memoria
    printf("n: %p\n", &n);
    printf("q: %p\n", q);
    printf("n= %i\n", n);

    // Desreferencia significa no tomar la direccion de memoria sino el valor almacenado en ella.
    *p = 80;

    printf("---------------------\n");
    printf("*p: %i\n", *p); // *p es acceder a los valores guardados en la direccion de memoria de n
    printf("*q: %i\n", *q);
    printf("n= %i\n", n);

    *q = 1;

    printf("---------------------\n");
    printf("*p: %i\n", *p);
    printf("*q: %i\n", *q);
    printf("n= %i\n", n);

    return 0;
}