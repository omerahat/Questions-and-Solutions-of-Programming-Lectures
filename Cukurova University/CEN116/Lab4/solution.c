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

int isupper(char ch){

    if(ch >= 'A' && ch <= 'Z')
        return 1;

    else 
        return 0;

}

int islower(char ch){

    if(ch >= 'a' && ch <= 'z')
        return 1;

    else 
        return 0;

}