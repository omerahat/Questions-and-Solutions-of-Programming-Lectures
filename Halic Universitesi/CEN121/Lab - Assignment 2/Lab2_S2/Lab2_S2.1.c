// Fig. 4.1: fig04_01.c
// Counter-controlled iteration
#include <stdio.h>

int main(void)
{
   unsigned int counter = 1; // initialization
   
   while (counter <= 10) { // iteration condition
      printf ("%u\n", counter); 
      ++counter; // increment
   }
} 
