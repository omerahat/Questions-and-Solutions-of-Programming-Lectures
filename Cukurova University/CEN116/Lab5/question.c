#include <stdio.h>

int isupper(char ch);
int islower(char ch);
char toupper(char ch);
char tolower(char ch);

int main(void){

    char ch;
    printf("Please enter a character:");
    ch = getchar();

    if(isupper(ch))
        printf("%c is an uppercase letter.\n", ch);
    
    else if (islower(ch))
        printf("%c is an lowercase letter.\n", ch);
     
    printf("%c to upper %c\n", ch, toupper(ch));
    printf("%c to lower %c\n", ch, tolower(ch));

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

char toupper(char ch){

    if(islower(ch))
        return ch - 32;
    
    else 
        return ch;
}

char tolower(char ch){

    if(isupper(ch))
        return ch + 32;
    
    else 
        return ch;
}
