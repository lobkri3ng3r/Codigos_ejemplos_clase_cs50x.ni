#include <stdio.h>

int main(void)
{
    FILE *input = fopen("/workspaces/87022089/ejemplo/input.txt", "r");
    if (input == NULL)
    {
        printf("Error al abrir archivo \n");
        return 1;
    }

    FILE *output = fopen("/workspaces/87022089/ejemplo/output.txt", "w");
    if (output == NULL)
    {
        printf("Error al abrir archivo");
        fclose(input);
        return 1;
    }

    char c;
    while (fread(&c, sizeof(char), 1, input))
    {
        
        fwrite(&c, sizeof(char), 1, output);
    }

    fclose(input);
    fclose(output);
}