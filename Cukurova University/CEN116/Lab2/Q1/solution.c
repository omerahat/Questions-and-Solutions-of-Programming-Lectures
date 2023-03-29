#include <stdio.h>

void bubleSort(int *, int);
void swap(int *, int *);

int main(){

    int array[10] = {2,168,5,93,18,9,4,79,27,45};
    int i;
    printf("Array in original order:\n");
    for (i=0; i<10; i++)
        printf("%4d", array[i]);


    return 0;
}