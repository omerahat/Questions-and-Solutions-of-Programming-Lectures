#include <stdio.h>

/* mystery function takes two unsigned integers as inputs and returns the result */
unsigned int mystery (unsigned int a, unsigned int b);

/* Main function to test the mystery function */
int main(void){
printf("%s", "Enter two positive integers: ");

/* Input variables */
unsigned int x;
unsigned int y;

 /* Read the two integers from the user */
scanf("%u%u", &x, &y);

/* Call the mystery function and print the result */
printf("The result is %u\n", mystery(x, y));

}

unsigned int mystery (unsigned int a, unsigned int b)
{
/* If b is equal to 1, return a */
if (1==b) {
return a;
}
/* If b is not equal to 1, return the sum of a and the result of the function called with (a, b-1) as inputs */
else {
return a + mystery (a, b-1);
}
}
