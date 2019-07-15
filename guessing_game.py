#!/usr/bin/env python3

from random import randint

def start_game():
    print("***Number Guessing Game***")

    random_number = randint(1, 50)
    while True:
        user_number = int(input("Guess a number: "))
        if user_number == random_number: break
        else:
            if user_number > random_number: print("It's lower")
            else: print("It's higher")
        print()

    print("You got it! The number was {}".format(random_number))
    
if __name__ == '__main__': start_game()
