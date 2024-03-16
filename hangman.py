import random
import tkinter as tk
from tkinter import messagebox

HANGMAN_STAGES = ['''
    +---+
         |
         |
         |
        ===''', '''
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
       ===''', r'''
    +---+
    O   |
   /|\  |
        |
       ===''', r'''
    +---+
    O   |
   /|\  |
   /    |
       ===''', r'''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

easy_words = 'ant bat cat dog fox lion frog bear bird duck'.split()
medium_words = 'monkey tiger camel zebra rhino elephant dolphin whale shark'.split()
hard_words = 'penguin kangaroo cheetah giraffe hippopotamus crocodile chimpanzee gorilla'.split()

def chooseRandomWord(word_list):
    """
    Returns a random word from the provided list of words.
    """
    index = random.randint(0, len(word_list) - 1)
    return word_list[index]

def displayBoard(missed_letters, correct_letters, secret_word):
    """
    Display the Hangman stage, missed letters, and the current state of the secret word.
    """
    canvas.itemconfig(hangman_image, image=HANGMAN_STAGES[len(missed_letters)])
    missed_label.config(text='Missed letters: ' + ' '.join(missed_letters))
    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    word_label.config(text=blanks)

def getPlayerGuess(already_guessed):
    """
    Prompt the player to guess a letter.
    Ensures the player enters a single letter and nothing else.
    """
    guess = entry.get().lower()
    if len(guess) != 1:
        messagebox.showinfo("Invalid Input", "Please enter only a single letter.")
        return None
    elif guess in already_guessed:
        messagebox.showinfo("Already Guessed", "You have already guessed that letter. Please try again.")
        return None
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        messagebox.showinfo("Invalid Input", "Please enter a letter from the alphabet.")
        return None
    else:
        return guess

def selectDifficulty():
    """
    Allows the player to choose the game difficulty level.
    """
    difficulty = tk.Toplevel()
    difficulty.title("Select Difficulty Level")
    difficulty.geometry("200x100")

    tk.Label(difficulty, text="Select difficulty level:").pack()
    tk.Radiobutton(difficulty, text="Easy", value=1, command=lambda: select_difficulty(difficulty, 1)).pack()
    tk.Radiobutton(difficulty, text="Medium", value=2, command=lambda: select_difficulty(difficulty, 2)).pack()
    tk.Radiobutton(difficulty, text="Hard", value=3, command=lambda: select_difficulty(difficulty, 3)).pack()

    difficulty.mainloop()

def select_difficulty(difficulty, choice):
    difficulty.destroy()
    global words
    if choice == 1:
        words = easy_words
    elif choice == 2:
        words = medium_words
    else:
        words = hard_words
    start_game()

def start_game():
    global missed_letters, correct_letters, game_is_done, secret_word

    # Initialize game variables
    missed_letters = ''
    correct_letters = ''
    game_is_done = False

    # Choose a random word from the selected word list
    secret_word = chooseRandomWord(words)

    # Display the initial game state
    displayBoard(missed_letters, correct_letters, secret_word)

# Create the main window
window = tk.Tk()
window.title("Hangman")

# Create a canvas to display the hangman image
canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()

# Create a label to display the missed letters
missed_label = tk.Label(window, text='Missed letters: ')
missed_label.pack()

# Create a label to display the current state of the secret word
word_label = tk.Label(window, text='')
word_label.pack()

# Create an entry field for the player to enter their guess
entry = tk.Entry(window)
entry.pack()

# Create a button to submit the player's guess
submit_button = tk.Button(window, text="Submit", command=lambda: handle_guess())
submit_button.pack()

def handle_guess():
    global missed_letters, correct_letters, game_is_done, secret_word

    guess = getPlayerGuess(missed_letters + correct_letters)
    if guess:
        if guess in secret_word:
            correct_letters += guess
            if all(letter in correct_letters for letter in secret_word):
                game_is_done = True
        else:
            missed_letters += guess
            if len(missed_letters) == len(HANGMAN_STAGES) - 1:
                game_is_done = True

        # Update the game state
        displayBoard(missed_letters, correct_letters, secret_word)

        # Check if the game is over
        if game_is_done:
            if all(letter in correct_letters for letter in secret_word):
                messagebox.showinfo("Game Over", "You win!")
            else:
                messagebox.showinfo("Game Over", "You lose. The word was " + secret_word)
            if playAgain():
                start_game()
            else:
                window.destroy()

# Asks the player if they want to play again.
def playAgain():
    response = messagebox.askyesno("Play Again?", "Would you like to play again?")
    return response

# Select the difficulty level
selectDifficulty()

# Start the mainloop
window.mainloop()
