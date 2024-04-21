#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

int main(void)
{
    string s1 = get_string("s1: ");
   int n = strlen(s1);

    for(int i = 0; i < n; i++)
    {
        printf("%c | ",s1[i]);
    }


   printf("\n");
   return 0;
}