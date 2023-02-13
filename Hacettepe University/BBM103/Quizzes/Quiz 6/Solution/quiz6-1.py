import sys
number = int(sys.argv[1])
def diamond_print(number, counter=None,counter2 =None):
    if number == 0:
        if counter2==None:
            counter2 = 0
        print((counter2+1)*' '+'*'*(counter-4))
        counter -= 2
        counter2+=1
        if counter <1:
            return
        diamond_print(number,counter,counter2)
    elif counter==None:
        counter = 1
        return diamond_print(number,counter)
    else:
        print((number-1)*' '+'*'*counter)
        counter += 2
        
        diamond_print(number-1,counter)

diamond_print(number)