#!/usr/bin/env python3

from random import randint

def start_game():
    guesses = 0
    print("***Number Guessing Game***")

    random_number = randint(1, 50)
    while True:
        try:
            user_number = int(input("Guess a number: "))
            guesses += 1

            if user_number == random_number: break
            else:
                if user_number > random_number: print("It's lower")
                else: print("It's higher")
        except ValueError: 
            print("Only integers are allowed\n")
            continue
        print()

    print("You got it! The number was {}".format(random_number))
    print("It took you {} guess(es).".format(guesses))
    
if __name__ == '__main__': start_game()
