#In this exercise I assumed True == 1 and False == 0, so True means odd and False means even
def odd_or_even(number):
    if number%2 == 0:  
          return False  
    else:    
        return True

def exercise1():
    number = int(input("Please enter a number."))
    counter = 0  
    odds = 0 
    evens = 0
    while(number!=0):
        if odd_or_even(number) == True:
            odds += number
        else:
            evens += number
            counter += 1
        number -= 1
    
    print('Odds are equal to: ', odds)
    if counter == 0:
        print('Average of evens are equal to: ', 0)
    else:
        print('Average of evens are equal to: ', int(evens/counter))    

exercise1()
