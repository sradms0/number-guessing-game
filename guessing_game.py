#!/usr/bin/env python3

from random import randint
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def menu(best_score, guesses, last_guess, message):
    print("***Number Guessing Game***")
    if best_score == 0: 
        best_score = "None"
    if last_guess == 0: 
        last_guess = "None"
    print(f"Last guess: {last_guess}")
    print(f"Guesses: {guesses}")
    print(f"Best score: {best_score}")
    print("[exit game: enter -1]")
    print()
    print(message)

def thank_you():
    print("Thanks for playing!\n")

def start_game():
    _min = 1
    _max = 50
    random_number = randint(_min, _max)
    user_number = 0
    guesses = 0
    best_score = 0
    play_count = 0
    message = ""

    while user_number != -1 and random_number != user_number:
        menu(best_score, guesses, user_number, message)
        # disallow conversion crashing
        try: user_number = int(input("Guess a number: "))
        except ValueError: 
            message = "Only integers are allowed"
            clear_screen()
            continue
        
        clear_screen()
        guesses += 1
        # user guessed right
        if user_number == random_number: 
            # notify user of win and ask to play again
            print(f"You got it! The number was {random_number}")
            print(f"It took you {guesses} guess(es)")
            play_again = input("Play again? [Y/N]: ").lower()
            play_count += 1

            if play_again == 'y': 
                # set best score to guesses on first game
                if play_count == 1: best_score = guesses
                elif guesses < best_score: best_score = guesses
                    
                # reset variables and display best score
                random_number = randint(_min, _max)
                user_number = 0
                guesses = 0
                message = ""
                clear_screen()
        # check input further
        else:
            # validate numeric input
            if user_number < _min or user_number > _max: 
                message = "Input is out of range"
                continue
            # provide hints
            elif user_number > random_number: message = "It's lower"
            else: message = "It's higher"

    thank_you()

if __name__ == '__main__': 
    try: start_game()
    except KeyboardInterrupt:  
        clear_screen()
        thank_you()
