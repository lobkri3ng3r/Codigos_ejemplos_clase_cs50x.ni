#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <cs50.h>

// Estructura de información contenida en los nodos
typedef struct nodo
{
    char nombre[10];
    struct nodo *siguiente;
    
} nodo;

int hash(string nombre);
void liberacion();

nodo *table[26];

int main()
{
    char c[10] ;
    // Cargar el diccionaio en modo lectura
    FILE *new = fopen("libreta.txt", "r");
    if (new == NULL)
    {
        // Si no exite, cerrar el archivo y retornar falso
        fclose(new);
        printf("Archivo no encontrado");
        return 1;
    }
    while (fscanf(new, "%s", c) != EOF)
    {
        // Guardar espacio para el nodo
        nodo *tmp = malloc(sizeof(nodo));
        // Si no hay espacio, retornar false
        //printf("%p\n",tmp);
        if (tmp == NULL)
        {
            return 1;
        }
        // Inicalizar nodo apuntando a NULL
        tmp->siguiente = NULL;
        strcpy(tmp->nombre, c);
        // Si la hash table esta vacia, converir tmp en mi primer nodo
        if (table[hash(c)] == NULL)
        {
            table[hash(c)] = tmp;
        }
        // Si no esta vacia, insertar por cabeza
        else
        {
            tmp->siguiente = table[hash(c)];
            table[hash(c)] = tmp;
        }
    }
    fclose(new);

    for (int j = 0; j < 26; j++)
    {
        printf("Índice: %d ->", j);
        for (nodo *aux = table[j]; aux != NULL; aux = aux->siguiente)
        {
            printf("%s ->", aux->nombre);
        }
        printf("NULL\n");
    }

    liberacion();
}

int hash(string nombre)
{
    nombre[0] = toupper(nombre[0]);
    int posicion = nombre[0] - 65;
    return posicion;
}

void liberacion()
{
    nodo *aux;
    for (int i = 0; i < 26; i++)
    {
        while (table[i] != NULL)
        {
            aux = table[i]->siguiente;
            free(table[i]);
            table[i] = aux;
        }
    }
}
