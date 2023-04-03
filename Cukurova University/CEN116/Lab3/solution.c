#include <stdio.h>
void swap(int *a, int *b);
int ascending(int a, int b);
int descending(int a, int b);
void bubble(int work[], int size, int (*compare)(int a, int b)); 

int main(void) { 

	int array[] = {3, 27, 18, 12, 9, 15, 6, 30, 24, 21}; 
	int i, order; 

	printf("Array in original order:\n"); 

	for (i = 0; i < 10; i++) { 
		printf("%4d", array[i]); 
	} 

	printf( "\nEnter 1 to sort in ascending order, 2 to sort in descending order: "); 
    scanf("%d", &order); 
    
    if (order == 1) 
        bubble(array, 10, ascending); 

    else 
        bubble(array, 10, descending); 

    printf("Array in order:\n"); 

    for (i = 0; i < 10; i++) { 
        printf("%4d", array[i]); 
    }

    return 0; 
} 

void swap(int *a, int *b) { 
    int temp; 
    temp = *a; *a = *b; 
    *b = temp; 
} 

int ascending(int a, int b) { 
    return a > b; 
} 

int descending(int a, int b) { 
    return a < b; 
} 

void bubble(int work[], int size, int (*compare)(int a, int b)) { 
    
    int count, pass; 

    for (pass = 0; pass < size - 1; pass++) { 

        for (count = 0; count < size - 1; count++){

            if ((*compare)(work[count], work[count + 1])) 
                swap(&work[count], &work[count + 1]);

        }

    } 

}