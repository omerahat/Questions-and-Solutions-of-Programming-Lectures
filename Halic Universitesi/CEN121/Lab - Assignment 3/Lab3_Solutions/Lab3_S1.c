#include<stdio.h>

int main()
{
    int a[3], i;
    
	printf("Enter 3 integer numbers\n");
	for(i = 0; i < 3; i++)
	    scanf("%d", &a[i]);
		
	printf("Array elements are: \n");
	for(i = 2; i >= 0; i--)
        printf("%10d", a[i]);

    return 0;
}
