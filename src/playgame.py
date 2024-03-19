'''
03/12/2024
Monica Nguyen
'''

# This code will using the python word list for the hangman game.
# The user could chose what catagories they wanted to guess the word,
# and will have the word random for them.

import wordlist

# Get a random word from the user choice of catgories
def chose_catagories():

    # Display the available word categories
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
    print("| 10. Foods                      |")
    print("|--------------------------------|")
    print("|  Other options:                |")
    print("|  e - Exit Program              |")
    print("+================================+")
    print()

    # Make sure user do the right syntax for accessing the dictionary, and option exit is available
    while True:
        choseCatagories = input("What category would you like to guess the word from? (choose a number between 1 and 10): ")
        # If user chose exit, break the loop
        if choseCatagories.lower() in ['e', 'exit']:
            print("Exiting the game...")
            return None
        elif not choseCatagories.isdigit():
            print("The input must be a number. Try again.")
        
        # User can only input number to match with the categories, which is only from 1 to 10
        # for 10 categories.
        else:
            choseCatagories = int(choseCatagories)
            if choseCatagories < 1 or choseCatagories > 10:
                print("The input must be a number from 1 to 10. Try again.")
            else:
                # Use the number to find in the word list dictionary. The number then will used
                # as an access key to the according Lists on wordlist.py
                word = wordlist.get_random_word_from_category(choseCatagories)
                return word.upper()

# Add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

# Draw the Hang man, also displaying every other infromation belong it.
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    HANGMAN_PICS = ['''
          +
          |
          |
          |
        ===''', '''
      +---+
          |
          |
          |
        ===''','''
      +---+
      O   |
          |
          |
        ===''', '''
      +---+
      O   |
      |   |
          |
        ===''', '''
      +---+
      O   |
     /|   |
          |
        ===''', '''
      +---+
      O   |
     /|\  |
          |
        ===''', '''
      +---+
      O   |
     /|\  |
     /    |
        ===''', '''
      +---+
      O   |
     /|\  |
     / \  |
        ===''']

    if num_wrong > 0:
        # Since the user must be wrong at least 1 to start the picture
        # So to match the index of pictures with the wrong, the index 
        # must be wrong-1 with wrong start from 1
        print(HANGMAN_PICS[num_wrong - 1])
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
    word = chose_catagories()

    # In case the user chose to exit from the categories, 
    # The code will be terminated as there is nothing to guess
    if word is None:
            print("\nBye !!")
            # Terminate the program
            return
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

    # Adding color code to change
    # ANSI escape code for green color
    green_code = '\033[92m'
    # ANSI escape code for red color
    red_code = '\033[91m'
    # ANSI escape code to reset color
    reset_code = '\033[0m'

    print("-" * 80)
    if remaining_letters == 0:
        print(green_code + "Congratulations! You got it in", 
               num_guesses, "guesses." + reset_code)
        
    else:    
        print(red_code + "Sorry, you lost." + reset_code)
        print(red_code + "The word was:", word + reset_code)

def main():
    # Asking for user name 
    name= input("What is your name ??: ")
    print("Hi "+ name + "!, Welcome to: ")
    print()

    # Display the game name
    print("==============================")
    print("Play the H A N G M A N game")
    print("==============================")
    print()

    play_again = True
    while play_again:
        play_game()
        print()
        
        while True:
            # Check syntax to make sure user only can answer yes or no.
            again = input("Do you want to play again (y/n)?: ")
            if again.lower() in ["y", "yes"]:
                break
            elif again.lower() in ["n", "no"]:
                print("Exiting the game...")
                play_again = False
                break
            else:
                # To break the loop, must answer y,yes,n,no
                print("Syntax error. Can only type 'y' for Yes and 'n' for No. Please try again.")
    
    print()
    print("Bye !!")

if __name__ == "__main__":
    main()
