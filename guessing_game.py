#!/usr/bin/env python3

from random import randint

def start_game():
    print("***Number Guessing Game***")
    _min = 1
    _max = 50
    random_number = randint(_min, _max)
    user_number = 0
    guesses = 0

    while random_number != user_number:
        try:
            user_number = int(input("Guess a number: "))

            if user_number < _min or user_number > _max: 
                print("Input is out of range\n")
                continue
            if user_number > random_number: print("It's lower")
            elif user_number < random_number: print("It's higher")
            guesses += 1

            if user_number == random_number: 
                print("You got it! The number was {}".format(random_number))
                print("It took you {} guess(es)".format(guesses))
                play_again = input("Play again? [Y/N]: ").lower()
                if play_again == 'y': 
                    random_number = randint(_min, _max)
                    user_number = 0
                    guesses = 0
                    print()
                    continue
                else: print("\nThanks for playing!")
        except ValueError: 
            print("Only integers are allowed\n")
            continue
        print()

if __name__ == '__main__': start_game()
