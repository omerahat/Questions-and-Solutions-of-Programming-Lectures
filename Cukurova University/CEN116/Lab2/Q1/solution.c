#include <stdio.h>
#define SIZE 10

void bubleSort(int *, int);
void swap(int *, int *);

int main(){

    int array[SIZE] = {2,168,5,93,18,9,4,79,27,45};
    int i;
    printf("Array in original order:\n");

    for (i=0; i<SIZE; i++)
        printf("%4d", array[i]);

    bubleSort(array, SIZE);

    return 0;
}

void bubleSort(int *array, const int size){

    int pass, j;
    for (pass=0; pass<size-1; pass++)
        for (j=0; j<size-1; j++)
            if(array[j] > array[j+1])

    swap(&array[j], &array[j+1]);
}