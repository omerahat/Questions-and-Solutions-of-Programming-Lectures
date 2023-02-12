/* lAB 5
Create 3 dimensional array 
Put the number 1- 5 in the array
Print the result
Take screenshot of your work
NO LATE Submission*/


#include <stdio.h>

int main()
{
    // Declaring a 3-dimensional array with 5 elements
    int array[2][2][2] = 
    {
        {{1, 2}, {3, 4}},
        {{5, 1}, {2, 3}}
    };

    // Printing the contents of the 3-dimensional array
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            for (int k = 0; k < 2; k++)
            {
                printf("array[%d][%d][%d] = %d\n", i, j, k, array[i][j][k]);
            }
        }
    }

    return 0;
}

/*If you can't run the code, try https://www.onlinegdb.com/. 
There is a compiler difference unfortunately :(*/
