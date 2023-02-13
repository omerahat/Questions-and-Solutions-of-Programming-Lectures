import sys

def sum_of_numbers_of_digits(number1, number2):
    if number1>=0 and number2>=0:
        square = number1 ** number2 #number1 is sys.argv[1], number2 is sys.argv[2]
        print('Output : {}^{} = {}'.format(number1,number2,square),end=" ")
        def reqrusion(square): #defines a new function
            sum_of_numbers = 0            
            if len(str(square))>1: #if this condition False, that means our number is one digit.(so program ends)
                digits = [int(i) for i in (str(square))] #creates a list named digits. which takes digits of square as individual elements
                sum_of_numbers = sum(digits) #sums all of the numbers of digits list
                print("=", end=" ")
                for i in digits[:-1]: #prints except the last element
                    print(i,'+',end=' ')
                print(digits[-1],end=' ') #prints last element
                print("=", sum_of_numbers,end=" ") #prints equal end sum of all numbers. For example: = 12

                if len(str(sum_of_numbers))>1: #if this condition False, that means our number is one digit.(so program ends)
                    return reqrusion(sum_of_numbers) #returns function to itself with input of sum_of_numbers.
                                                    #that means our code runs again with output of previous loop 
                                                    #until it reachs one digit.

        reqrusion(square) #calls reqrusion function with square input
    else:
        print('ERROR! Only enter positive numbers!')
sum_of_numbers_of_digits(int(sys.argv[1]),int(sys.argv[2]))
