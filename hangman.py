import random

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

easy_words = 'Bird Jump Desk Fish Cake Chair Plant House River Smile Cloud Paper Apple Happy Music Turtle Rabbit Garden Orange Window'.split()
medium_words = 'Mango Rhino Puzzle Ocean Chair Coral Forest Castle Unicorn Diamond Wizard Mosaic Canyon Journey Crystal Desert Spirit Glacier Mystery Rainbow Miracle'.split()
hard_words = 'Planetarium Dimensional Democracy Algorithm Exquisite Tyrannosaur Octagonal Nucleotide Labyrinth Barricade Quasar Kaleidoscope Extraterrestrial Dystopian Paradoxical Phenomenon Obelisk Holographic Renaissance Infiltrate Bibliophile'.split()

def chooseRandomWord(word_list):
    """
    Returns a random word from the provided list of words.
    """
    index = random.randint(0, len(word_list) - 1)
    return word_list[index]

def displayBoard(missed_letters, correct_letters, secret_word):
    print()
    print(HANGMAN_STAGES[len(missed_letters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    # Display the secret word with spaces between the letters:
    for letter in blanks:
        print(letter, end=' ')
    print()

def getPlayerGuess(already_guessed):
    """
    Prompt the player to guess a letter.
    Ensures the player enters a single letter and nothing else.
    """
    while True:
        print('Please guess a letter:')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter only a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Please try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter from the alphabet.')
        else:
            return guess

def selectDifficulty():
    """
    Allows the player to choose the game difficulty level.
    """
    while True:
        print("Select difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        choice = input()
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def playAgain():
    """
    Asks the player if they want to play again.
    """
    print('Would you like to play again? (yes/no)')
    return input().lower().startswith('y')

print('|_H_A_N_G_M_A_N_|')
missed_letters = ''
correct_letters = ''
difficulty = selectDifficulty()
if difficulty == 1:
    words = easy_words
elif difficulty == 2:
    words = medium_words
else:
    words = hard_words

secret_word = chooseRandomWord(words)
game_is_done = False

while True:
    displayBoard(missed_letters, correct_letters, secret_word)
    guess = getPlayerGuess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters += guess
        if all(letter in correct_letters for letter in secret_word):
            print('You guessed it!')
            print('The secret word is "' + secret_word + '". You win!')
            game_is_done = True
    else:
        missed_letters += guess
        if len(missed_letters) == len(HANGMAN_STAGES) - 1:
            displayBoard(missed_letters, correct_letters, secret_word)
            print('You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was "' + secret_word + '".')
            game_is_done = True

    if game_is_done:
        if playAgain():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            difficulty = selectDifficulty()
            if difficulty == 1:
                words = easy_words
            elif difficulty == 2:
                words = medium_words
            else:
                words = hard_words
            secret_word = chooseRandomWord(words)
        else:
            break
