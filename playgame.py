'''
DEV 108 Final Project
03/12/2024
Monica Nguyen
'''

# THIS CODE SKELETON HAS BEEN IMPORTED FROM 'ch10 > hangman.py'

# This code will using the python word list for the hangman game.
# The user could chose what catagories they wanted to guess the word,
# and will have the word random for them.

import wordlist

# Get a random word from the user choice of catgories
def chose_catagories():
    print("+================================+")
    print("|         WORD CATEGORIES        |")
    print("|--------------------------------|")
    print("|  Pick a theme to play:         |")
    print("|  1. Animals                    |")
    print("|  2. Fruits                     |")
    print("|  3. Colors                     |")
    print("|  4. Countries                  |")
    print("|  5. Sports                     |")
    print("|  6. Occupations                |")
    print("|  7. Vehicles                   |")
    print("|  8. Planets                    |")
    print("|  9. Movies                     |")
    print("|  10. Foods                     |")
    print("+================================+")
    print()
    choseCatagories= input("What categories you like to guess the word from? (chose a number): ")
    if int(choseCatagories) <= 0 and int(choseCatagories) > 10:
        print("Wrong syntax. The input must be a number from 1 to 10. Try again")
        choseCatagories= input("What categories you like to guess the word from? (chose a number): ")
    else:
        word = wordlist.get_random_word_from_category(choseCatagories)
        return word.upper()

# Add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

# Draw the display
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("-" * 80)
    print("Word:", add_spaces(displayed_word),
          "  Guesses:", num_guesses,
          "  Wrong:", num_wrong,
          "  Tried:", add_spaces(guessed_letters))

# Get next letter from user
def get_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().upper()
    
        # Make sure the user enters a letter and only one letter
        if guess == "" or len(guess) > 1:
            print("Invalid entry. " +
                  "Please enter one and only one LETTER.")
            continue
        # Don't let the user try the same letter more than once
        elif guess in guessed_letters:
            print("You already tried that LETTER.")
            continue
        else:
            return guess

# The input/process/draw technique is common in game programming
def play_game():
    word = get_word()
    
    word_length = len(word)
    remaining_letters = word_length
    displayed_word = "_" * word_length

    num_wrong = 0               
    num_guesses = 0
    guessed_letters = ""

    draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    while num_wrong < 8 and remaining_letters > 0:
        guess = get_letter(guessed_letters)
        guessed_letters += guess
        
        pos = word.find(guess, 0)
        if pos != -1:
            displayed_word = ""
            remaining_letters = word_length
            for char in word:
                if char in guessed_letters:
                    displayed_word += char
                    remaining_letters -= 1
                else:
                    displayed_word += "_"              
        else:
            num_wrong += 1

        num_guesses += 1

        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    print("-" * 80)
    if remaining_letters == 0:
        print("Congratulations! You got it in", 
               num_guesses, "guesses.")   
    else:    
        print("Sorry, you lost.")
        print("The word was:", word)

def main():
    name= input("What is your name ??: ")
    print("Hi "+ name + "!, Welcome to")
    print()
    print("==============================")
    print("Play the H A N G M A N game")
    print("==============================")
    print()
    while True:
        play_game()
        print()
        again = input("Do you want to play again (y/n)?: ").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()
