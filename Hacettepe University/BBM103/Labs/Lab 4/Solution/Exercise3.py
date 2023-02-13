import random

def random_number_guessing_game():
    number = random.randint(1,25)
    print("Secret number is between 1 and 25.")
    while(True):   
        guess = int(input("Guess it!"))

        if number == guess:
            print("Number was {}. Congratulations, you guessed it corretly!".format(number))          
            break
        elif number > guess:
            print("Increase your number.")
        elif number < guess:
            print("Decrease your number")  

random_number_guessing_game()
