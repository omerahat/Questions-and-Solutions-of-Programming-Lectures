import argparse
import sys

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("integer1_to_sum", help="display a summation of the given numbers", type=int)
    parser.add_argument("integer2_to_sum", help="display a summation of the given numbers", type=int)
    args = parser.parse_args()

    #print the square of user input from cmd line.
    print("Summation of the numbers: ",args.integer1_to_sum + args.integer2_to_sum)

    #print all the sys argument passed from cmd line including the program name.
    print("List of program name and system arguments: ",sys.argv)

    #print the second argument passed from cmd line; Note it starts from ZERO
    print("The second argument: ",sys.argv[1])

except Exception as e:
    print(e)
#except:
    #e = sys.exc_info()[0]
    #print(e)
    
    
