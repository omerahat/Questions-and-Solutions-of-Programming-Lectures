#! /usr/bin/python3
number = int(input("Please enter the number to convert binary format: "))
if number>0:
    remainder, main_number = "", number
    while number!=0:
        remainder = remainder+str(number%2)
        number = number//2
    print("Binary of {} is:".format(main_number),remainder[::-1])
else:
    print("Please enter a positive number!")
