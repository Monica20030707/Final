# Hangman Game

This is a simple Python implementation of the classic word-guessing game. In Hangman, players try to guess a hidden word letter by letter. With each incorrect guess, a part of the hangman is drawn. The game ends when the player successfully guesses the word or runs out of guesses, resulting in the hangman being fully drawn.

## How to Play

Follow the on-screen instructions to play the game:

1. **Choose a word category** by entering a number between 1 and 10.
2. **Enter a letter** to guess the word.
3. **Continue guessing** until you solve the word or make too many incorrect guesses.
4. **Choose whether to play again** after finishing a game.

## Functions

### `chose_catagories()`

Allows the user to select a word category from a list of available categories. It prompts the user to input a number corresponding to the desired category and returns a random word from the chosen category.

### `add_spaces(word)`

Takes a word as input and returns the word with spaces between each letter. This is useful for displaying the word with spaces in the hangman game.

### `draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)`

Draws the hangman figure based on the number of wrong guesses (`num_wrong`). It also displays the current state of the game, including the number of guesses, letters guessed, and the partially revealed word.

### `get_letter(guessed_letters)`

Prompts the user to input a letter for guessing. It ensures that the input is a single letter that hasn't been guessed before and returns the guessed letter.

### `play_game()`

Orchestrates the hangman game. It calls other functions to choose a word category, manage game state, handle user input, and display game information. It continues the game until the player wins or loses.

### `main()`

Entry point of the program. Greets the user, displays the game title, and starts the game loop. After each game, it asks the user if they want to play again and handles their response accordingly.
