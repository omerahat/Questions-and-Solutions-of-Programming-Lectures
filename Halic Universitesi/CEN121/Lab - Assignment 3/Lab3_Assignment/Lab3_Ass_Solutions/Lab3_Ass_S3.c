#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {     //declares the main function, which is the starting point of the program
	int n;       //declares a variable n of type int
	
	printf("random number in [0,19]\n");  //prints the string "random number in [0,19]" to the console
	 
	srand(time(NULL));   //seeds the random number generator with the current time
	n =  rand() % 20;    //generates a random number in the range [0, 19]
	printf("%d\n", n);   //prints the value of n to the console
	 
	return 0;            //ends the main function and returns 0 to indicate successful completion of the program
}
