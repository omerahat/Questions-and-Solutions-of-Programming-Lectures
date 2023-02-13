#include <stdio.h>

int main( void )
{
    int outer_count = 1; // initialize count 
    while ( outer_count <= 10 ) { // loop 10 times 
   
    int inner_count = 1; 
	while ( inner_count <= outer_count ) { 
   
    printf( "*" );
    inner_count++; 
 } // end inner while
   
    printf( "\n" );
    outer_count++; 
 } // end outer while
} // end main 

