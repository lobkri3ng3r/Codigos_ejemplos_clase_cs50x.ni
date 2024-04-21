#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s1 = get_string("S1: ");
    int n = strlen(s1);

    for (int i = 0; i < n; i++)
    {
        if(isdigit(s1[i]))
        {
            printf("%c --> Es un digito \n",s1[i]);
        }

        if(isalpha(s1[i]))
        {
            printf("%c --> Es una letra \n",s1[i]);
        }

        if(isspace(s1[i]))
        {
            printf("%c --> Es una espacio \n",s1[i]);
        }

        // printf("%c | ",toupper(s1[i]));
    }

    printf("\n");

}