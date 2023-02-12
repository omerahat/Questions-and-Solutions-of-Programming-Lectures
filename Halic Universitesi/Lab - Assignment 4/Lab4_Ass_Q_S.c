/* Assignment 4
Write C program
1- put your full name in array.
2- print it from left to right.
3- print it from right to left.*/


#include <stdio.h> 
#include <stdlib.h> 

int main()
{
    int i, j;
	char text[20];  // Declaring a character array to store the user's name
    
	printf("Write your name: ");  // Prompting the user to input their name

    scanf("%s",&text);  // Reading the user's name into the text array

    printf("\nYour name : ");   // Printing the user's name

	for(i=0; text[i] != 0; i++)  // Loop to print each character of the user's name	

    {   
	printf("%c",text[i]);   // Printing the current character
  }  
  printf("\nReverse of your name: "); // Printing the label for the reversed name

  for(j=i; j >= 0; j--) // Loop to print the characters of the name in reverse order
{
  printf("%c",text[j]); // Printing the current character in reverse order 
}
return 0;  // Printing the label for the reversed name
}
