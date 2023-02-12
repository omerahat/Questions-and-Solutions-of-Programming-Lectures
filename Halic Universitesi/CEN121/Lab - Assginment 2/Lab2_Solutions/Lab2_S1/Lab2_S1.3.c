#include <stdio.h>
#include <stdlib.h>

int main() 
{
    char name[15]; // account name
	printf ("Enter Your Name: "); // prompt for input
	scanf("%s", name); // read name from user
	
	int a,b,c,d,p; // a,b,c,d,p values
	
	printf("Enter Numbers: "); // prompt for input
	scanf("%d""%d""%d""%d", &a,&b,&c,&d); // read numbers from user
	
	p=a*b*c*d; 
	printf("%d\n", p); // prompt for input
	
	int x,y; // x,y values
	printf("Enter Numbers: "); // prompt for input
	scanf("%d""%d", &x,&y);  // read numbers from user
	
	if (x>y)
	{
     	x=10; // assign 10 to x
	    printf("new value: %d\n", x); // display new value
    } // end if
	
	else 
   {
	     x=20; // assign 20 to x
		 printf("new value: %d\n", x);  // display new value
    } // end else
} // end function main


