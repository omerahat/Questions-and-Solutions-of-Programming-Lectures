#include <stdio.h> 
#include <stdlib.h> 
#include <ctype.h>

int main() {
  
  char s[6][100]; // Declare a 20 character array to hold the strings 
  
  double values[6]; // Declare a double array to hold the converted values 
  
  double sum = 0; // Declare and initialize a variable to hold the sum
  
  printf("Enter six floating-point values: "); // Prompt the user for input 
  
  for (int i = 0; i < 6; i++) { // Loop through the strings 
       
	   scanf("%s", s[i]); // Read a string from the user
       
	   values[i] = strtod(s[i], NULL); // Convert the string to a double and store it in the values array
       
	sum += values[i]; // Add the converted value to the sum
}
  
  printf("Sum: %.2f\n", sum); // Output the sum as a float with two decimal places
  
  printf("Average: %.2f\n", sum/6); // Output the average as a float with two decimal places

  return 0;
}

#include <stdio.h> 
#include <stdlib.h> 
#include <ctype.h>

int main() {
  
  char s[6][100]; // Declare a 20 character array to hold the strings 
  
  double values[6]; // Declare a double array to hold the converted values 
  
  double sum = 0; // Declare and initialize a variable to hold the sum
  
  printf("Enter six floating-point values: "); // Prompt the user for input 
  
  for (int i = 0; i < 6; i++) { // Loop through the strings 
       
	   scanf("%s", s[i]); // Read a string from the user
       
	   values[i] = strtod(s[i], NULL); // Convert the string to a double and store it in the values array
       
	sum += values[i]; // Add the converted value to the sum
}
  
  printf("Sum: %.2f\n", sum); // Output the sum as a float with two decimal places
  
  printf("Average: %.2f\n", sum/6); // Output the average as a float with two decimal places

  return 0;
}

/*
If doesn't work in Dev C++ use https://www.onlinegdb.com/. 
Compiler can notice :(
*/
