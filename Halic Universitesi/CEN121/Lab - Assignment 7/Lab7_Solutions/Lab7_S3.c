#include <stdio.h>
#include <string.h>

int main() {
  
  char s1[100], s2[100]; // Declare two character arrays to hold the strings
  
  printf("Enter the first string: "); // Prompt the user for input
  
  fgets(s1, sizeof(s1), stdin); // Read the first string from the user
  
  s1[strcspn(s1, "\n")] = '\0'; // Remove the newline character at the end of the string

  printf("Enter the second string: "); // Prompt the user for input

  fgets(s2, sizeof(s2), stdin); // Read the second string from the user

  s2[strcspn(s2, "\n")] = '\0'; // Remove the newline character at the end of the string

  printf("Before concatenation: \n");  
  printf("String 1: %s\n", s1); // Output the first string
  printf("String 2: %s\n", s2); // Output the second string

  strcat(s1, s2); // Concatenate the two strings
  
  printf("After concatenation: \n");
  
  printf("Concatenated string: %s\n", s1); // Output the concatenated string 
  
  printf("Length of concatenated string: %lu\n", strlen(s1)); // Output the length of the concatenated string

return 0;

}

/*
If doesn't work in Dev C++ use https://www.onlinegdb.com/. 
Compiler can notice :(
*/
