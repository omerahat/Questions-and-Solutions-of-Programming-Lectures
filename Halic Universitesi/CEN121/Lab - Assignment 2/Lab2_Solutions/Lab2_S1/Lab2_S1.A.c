#include <stdio.h>

int main()
{
    int sales; // sales to be read from user

	printf ("Enter Sales;"); 
	scanf ("%d", &sales); // read sales
	
	if ( sales >= 5000)  

    {

    puts("Sales are greater than or equal to $5000" );  // if sales are greater than or equal to $5000 writes this to the screen
	
	} // end if   
	
	else

	{

	puts("Sales are less than $5000" );  // if sales are less than $5000 writes this to the screen
   
    } // end if else
    
} // end function main
