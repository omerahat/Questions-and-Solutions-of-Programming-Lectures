#include <stdio.h> 
#include <ctype.h>

int main() {
  char s[100]; // Declare character array with maximum size of 100

  printf("Enter a line of text: "); // Prompt the user for input 
  fgets(s, sizeof(s), stdin); // Read a line of text from the user

  for (int i = 0; s[i] != '\0'; i++) {   // Loop through the characters in the array 
  if (i % 2 == 0) {   // If the index is even
  printf("%c", toupper(s[i])); // Output the character in uppercase

  }
  else {       // If the index is odd
  printf("%c", tolower(s[i])); // Output the character in Lowercase
 }
}

printf("\n"); // Output a newline at the end

return 0;
}

/*If doesn't work in Dev C++ use https://www.onlinegdb.com/.
 Compiler can notice :(*/
