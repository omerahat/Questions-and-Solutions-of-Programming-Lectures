#include <stdio.h>

//A program that prints the sum of all digits from 1 to 5, including 5, multiplied by itself.

int main( void ) 
{ 
    int x = 1;       
    int total = 0;
    while ( x <= 5 ) // iteration condition
    {
	   total+= x*x; // assign the product of the digits to the total and increase one
       
	   printf( "%d\n", x*x);
	   ++x;  // increment
	
	} // end while
    printf( "Total is %d\n", total);
} // end function main
