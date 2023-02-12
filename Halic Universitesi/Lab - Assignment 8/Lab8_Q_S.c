/*
LAB 8
Do the same program you had in class
With only one exam.
Enter 10 students.
*/


#include <stdio.h>  // Include the standard input/output library

#define S 50  // Define the constant S with the value 50

struct student // Define the struct student with a name field of 30 characters and an exam field of integer

{
   char name[30]; 
   int exam;
};

// The main function
int main() {
    int n;     // Declare integer variable n to store the number of students

	struct student st[S]; 	// Declare an array of struct student with a size of S

	printf("Enter Number Of The Student: ");  // Prompt the user to enter the number of students

	scanf("%d", &n); 	// Read the input and store it in n

	// Loop through the number of students
    for (int i = 0; i < n; i++) {
        
		printf("Enter Student Name %d: ", i+1);  // Prompt the user to enter the name of the student
		
		scanf("%s", st[i].name);   // Read the input and store it in the name field of the struct
		
		printf("Enter Students Mark %d: ", i+1); 	// Prompt the user to enter the exam mark of the student
		
		scanf("%d", &st[i].exam); 	// Read the input and store it in the exam field of the struct
    } 
    // Loop through the number of students
    for (int i = 0; i < n; i++) {
    	
		printf("Student %d: %s\n", i+1, st[i].name);  // Print the name of the student
		
		printf("Exam: %d\n", st[i].exam); 	// Print the exam mark of the student

 }

return 0; // Return 0 to indicate successful execution

}

/*
If doesn't work in Dev C++ use https://www.onlinegdb.com/. 
Compiler can notice :(
*/
