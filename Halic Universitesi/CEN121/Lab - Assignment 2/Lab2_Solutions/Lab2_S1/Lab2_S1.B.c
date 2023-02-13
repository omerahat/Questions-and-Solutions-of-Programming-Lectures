#include <stdio.h>
#include <stdlib.h>

int main() 
{
    int product, x; // product and x to be read from user
	x=1; // set x
	product = 0; // set product
	
	while ( x <= 10 ) // loop while x is less than or equal to 10 
	{
	product *= x; // multiply product by x 
	++x; // increment x 
	printf ("%d\n", product); // display product
	
	} // end while
	
} // end function main

