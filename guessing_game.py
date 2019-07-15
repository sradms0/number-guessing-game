#!/usr/bin/env python3

from random import randint

def start_game():
    guesses = 0
    _min = 1
    _max = 50
    print("***Number Guessing Game***")

    random_number = randint(_min, _max)
    while True:
        try:
            user_number = int(input("Guess a number: "))

            if user_number < _min or user_number > _max: 
                print("Input is out of range\n")
                continue

            if user_number == random_number: break
            else:
                if user_number > random_number: print("It's lower")
                else: print("It's higher")
        except ValueError: 
            print("Only integers are allowed\n")
            continue

        guesses += 1
        print()

    print("You got it! The number was {}".format(random_number))
    print("It took you {} guess(es).".format(guesses))
    
if __name__ == '__main__': start_game()
