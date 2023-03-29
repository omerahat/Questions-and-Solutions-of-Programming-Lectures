#include <stdio.h>
#define SIZE 10

void bubleSort(int *, int);
void swap(int *, int *);

int main(){

    int array[SIZE] = {2, 68, 5, 93, 18, 9, 4, 79, 27, 45};
    int i;
    printf("Array in original order:\n");

    for (i=0; i<SIZE; i++)
        printf("%3d", array[i]);

    bubleSort(array, SIZE);
    printf("\nArray in ascending order:\n");

    for (i=0; i<SIZE; i++)
        printf("%3d", array[i]);

    return 0;
}

void bubleSort(int *array, const int size){

    int pass, j;
    for (pass=0; pass<size-1; pass++)
        for (j=0; j<size-1; j++)
            if(array[j] > array[j+1])

    swap(&array[j], &array[j+1]);

}

void swap(int *ptr1, int *ptr2){

    int temp = *ptr1;
    *ptr1 = *ptr2;
    *ptr2 = temp;

}