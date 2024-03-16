import random
import tkinter as tk
from tkinter import messagebox

# Hangman stages to display
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

# Lists of words for different difficulty levels
easy_words = 'Bird Jump Desk Fish Cake Chair Plant House River Smile Cloud Paper Apple Happy Music Turtle Rabbit Garden Orange Window'.split()
medium_words = 'Mango Rhino Puzzle Ocean Chair Coral Forest Castle Unicorn Diamond Wizard Mosaic Canyon Journey Crystal Desert Spirit Glacier Mystery Rainbow Miracle'.split()
hard_words = 'Planetarium Dimensional Democracy Algorithm Exquisite Tyrannosaur Octagonal Nucleotide Labyrinth Barricade Quasar Kaleidoscope Extraterrestrial Dystopian Paradoxical Phenomenon Obelisk Holographic Renaissance Infiltrate Bibliophile'.split()

def chooseRandomWord(word_list):
    """
    Returns a random word from the provided list of words.
    """
    return random.choice(word_list)

def displayBoard():
    # Clear the canvas
    hangman_canvas.delete("all")
    # Display game elements on the canvas
    hangman_canvas.create_text(200, 20, text="HANGMAN", font=('Helvetica', 20, 'bold'), fill='black')
    hangman_canvas.create_text(200, 50, text='Missed letters: ' + ' '.join(missed_letters), font=('Helvetica', 12), fill='black')
    # Display the current state of the word being guessed
    word_display = ' '.join(letter if letter.lower() in correct_letters else '_' for letter in secret_word)
    hangman_canvas.create_text(200, 100, text=word_display, font=('Helvetica', 16), fill='black')
    # Display the hangman stage based on the number of missed letters
    hangman_canvas.create_text(200, 150, text=HANGMAN_STAGES[len(missed_letters)], font=('Courier', 12), anchor=tk.CENTER, fill='black')

def checkGuess():
    global game_is_done
    # Get the guess from the entry and convert it to lowercase
    guess = guess_entry.get().lower()
    if len(guess) != 1 or guess not in 'abcdefghijklmnopqrstuvwxyz':
        messagebox.showerror("Invalid Guess", "Please enter a single letter from the alphabet.")
    elif guess in missed_letters or guess in correct_letters:
        messagebox.showinfo("Already Guessed", "You have already guessed that letter. Please try again.")
    elif guess in secret_word.lower():  # Convert secret_word to lowercase for comparison
        correct_letters.add(guess)
        if set(secret_word.lower()) <= correct_letters:  # Convert secret_word to lowercase for comparison
            messagebox.showinfo("Congratulations", "You guessed it!\nThe secret word is '{}'.".format(secret_word))
            game_is_done = True
    else:
        missed_letters.add(guess)
        if len(missed_letters) == len(HANGMAN_STAGES) - 1:
            messagebox.showinfo("Game Over", "You have run out of guesses!\nThe word was '{}'.".format(secret_word))
            game_is_done = True
    displayBoard()
    guess_entry.delete(0, 'end')

def startGame():
    global words, secret_word
    if difficulty.get():
        if difficulty.get() == "easy_words":
            words = easy_words
        elif difficulty.get() == "medium_words":
            words = medium_words
        elif difficulty.get() == "hard_words":
            words = hard_words
        secret_word = chooseRandomWord(words)
        displayBoard()
    else:
        messagebox.showerror("Error", "Please select a difficulty level.")

root = tk.Tk()
root.title("Hangman Game")
root.configure(bg='beige')  # Set background color to beige

# Create a canvas for displaying the game elements
hangman_canvas = tk.Canvas(root, width=400, height=200, bg='beige')
hangman_canvas.pack()

# Initialize variables
missed_letters = set()
correct_letters = set()
difficulty = tk.StringVar()
words = []
secret_word = ''
game_is_done = False

# Create GUI elements
difficulty_label = tk.Label(root, text="Select difficulty level:", bg='beige')
difficulty_label.pack()

easy_button = tk.Radiobutton(root, text="Easy", variable=difficulty, value="easy_words", bg='beige')
easy_button.pack()

medium_button = tk.Radiobutton(root, text="Medium", variable=difficulty, value="medium_words", bg='beige')
medium_button.pack()

hard_button = tk.Radiobutton(root, text="Hard", variable=difficulty, value="hard_words", bg='beige')
hard_button.pack()

start_button = tk.Button(root, text="Start Game", command=startGame, bg='beige')
start_button.pack()

guess_label = tk.Label(root, text="Enter your guess:", bg='beige')
guess_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

submit_button = tk.Button(root, text="Submit Guess", command=checkGuess, bg='beige')
submit_button.pack()

# Start the tkinter event loop
root.mainloop()
