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