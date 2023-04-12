#include <stdio.h>

int isupper(char ch);
int islower(char ch);

int main(void){

    char ch;
    printf("Please enter a character: ");
    ch = getchar();

    if(isupper(ch))
        printf("%c is an uppercase letter.\n", ch);

    else if(islower(ch))
        printf("%c is an lowercase letter.\n", ch);

    return 0;
}