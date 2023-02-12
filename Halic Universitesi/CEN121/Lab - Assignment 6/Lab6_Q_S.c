/*Lab 6 - Sort the following no. in descending orders.
5, 1, 6, 7, 3, 2, 4, 8, 9, 0 */


#include <stdio.h>

// function to sort an array using bubble sort
void bubble_sort(int arr[], int n) {
  
   int i, j, temp; // declare variables for loop counters and temporary storage
   
    // outer loop to repeat the sorting process n-1 times
   for (i = 0; i < n - 1; i++) {
   // inner loop to compare and swap adjacent elements
   for (j = 0; j < n - i - 1; j++) {  
    // if the current element is greater than the next element
   if (arr[j] < arr[j+1]) { 
   
   temp = arr[j];   // swap the elements using a temporary variable
   
   arr[j] = arr[j + 1]; 
   
   arr[j+1] = temp;
   }
  }
 }
}
   // main function to test the bubble sort function
   int main(){
   
   int arr[] = {5, 1, 6, 7, 3, 2, 4, 8, 9, 0}; // declare and initialize an array of integers
   
   int n = sizeof(arr) / sizeof(arr[0]); // calculate the number of elements in the array
   
   bubble_sort(arr, n);   // call the bubble sort function to sort the array
   
   int i;  // declare a loop counter
   
   // loop to print the sorted array
   for (i = 0; i < n; i++) { 
   
   printf("%d ", arr[i]); 
   
   }

   printf("\n");  // add a newline for readability
   
   return 0; // return 0 to indicate successful execution of the program
}
