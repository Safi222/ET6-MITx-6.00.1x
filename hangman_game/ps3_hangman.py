# This Module implement interactive Hangman game between a player and the computer. 


import random
import string

WORDLIST_FILENAME = "./words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord=str, lettersGuessed=list):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
      if letter not in lettersGuessed:
        return False
    return True


def getGuessedWord(secretWord=str, lettersGuessed=list):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    player_guess = ""
    for letter in secretWord:
      if letter in lettersGuessed:
        player_guess += letter
      else :
        player_guess += "_"
        
    return player_guess



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # string.ascii_lowercase
    avaliable_letters = ""
    for letter in string.ascii_lowercase:
      if letter not in lettersGuessed:
        avaliable_letters += letter
      
    return avaliable_letters 
      
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secretWord)} letters long.")


    guesses = 8
    guessed_letters = [] 
    
    while guesses > 0:
      print("-------------")
      print(f"You have {guesses} guesses left.")
      print("Available letters:", getAvailableLetters(guessed_letters))
      
      user_guess = input("Please guess a letter: ").lower()

      
      if user_guess in guessed_letters:   
        print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, guessed_letters))
        continue
      
      guessed_letters.append(user_guess)
      if user_guess in secretWord:
        print("Good guess: ", getGuessedWord(secretWord, guessed_letters))      
        
      else :
        print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, guessed_letters))
        guesses -= 1

      if isWordGuessed(secretWord, guessed_letters):
        print("-------------")
        print(f"Congratulations, you won!. Secret word is{secretWord}")
        return
            
    print("-------------")
    print(f"Sorry, you ran out of guesses. The word was{secretWord}")


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
