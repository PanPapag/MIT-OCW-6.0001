# Problem Set 2, hangman.py

# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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
    print(str(len(wordlist)) + " words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_letter_guessed(secret_word,letter):
    for char in secret_word:
            if char == letter:
                return True
    return False

def unique_letters_in_word(secret_word):
    L = []
    counter = 0
    for char in secret_word:
        if char not in L:
            L.append(char)
            counter += 1
    return counter

def is_vowel(letter):
    Vowels = ['a','e','i','o']
    if letter in Vowels:
        return True
    else:
        return False


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False;
    return True;


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # initialize an empty list with the length of the secret_word
    L = ['_ '] * len(secret_word)
    n = 0
    for char in secret_word:
        if char in letters_guessed:
            L[n] = char
        n += 1
    # convert list to string and return it
    strL = ''.join(L)
    return strL



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # create a list with all the lowercase letters
    L = list(string.ascii_lowercase)

    for char in letters_guessed:
        # if letter on the list remove it
        if char in string.ascii_lowercase:
            L.remove(char)
    # convert list to string and return it
    strL = ''.join(L)
    return strL




def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    # initialize variables
    guesses_left = 6
    warnings = 3
    letters_guessed = []
    while guesses_left != 0 and is_word_guessed(secret_word,letters_guessed) == False:
        print("--------------------------------------------------")
        print("You have " + str(guesses_left) + " guesses left.")
        print("Availabe letters: " + get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ")
        # convert letter to lower so as to handle only lowercase characters
        letter = letter.lower()
        # assuring rule 2
        if letter.isalpha() == False:
            if(warnings != 0):
                warnings = warnings - 1
                print("Oops! That is not a valid letter. You now have " + str(warnings) + " warnings: " + get_guessed_word(secret_word,letters_guessed))
                continue
            else:
                print("Oops! That is not a valid letter: " + get_guessed_word(secret_word,letters_guessed))
                guesses_left = guesses_left - 1
                continue
        # assuring rule 3
        if letter not in letters_guessed:
            # append the letter in the list if and only if it has not been added Before
            letters_guessed.append(letter)
        else:
            # user has already guessed this letter
            if(warnings != 0):
                warnings = warnings - 1
                print("Oops! You 've already guessed that letter. You now have " + str(warnings) + " warnings: " + get_guessed_word(secret_word,letters_guessed))
                continue
            else:
                print("Oops! You 've already guessed that letter. You now have no warnings left, so you lose one guess: " + get_guessed_word(secret_word,letters_guessed))
                guesses_left = guesses_left - 1
                continue

        if(is_letter_guessed(secret_word,letter)):
            print("Good guess: " + get_guessed_word(secret_word,letters_guessed))
        else:
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word,letters_guessed))
            # reduce guesses_left by one if is consonant
            if(is_vowel(letter) == False):
                guesses_left = guesses_left - 1
            # reduce guesses_left by two if is vowel
            else:
                guesses_left = guesses_left - 2



    print("-------------")
    if guesses_left == 0:
        print("Sorry, you ran out of guesses. The word was else.")
    else:
        print("Congratulations, you won!")
        total_score = guesses_left * unique_letters_in_word(secret_word)
        print("Your total score for this game is: " + str(total_score))

# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    if len(my_word) != len(other_word):
        return False

    for index in range(len(my_word)):
        if my_word[index] == '_':
            if other_word[index] in my_word:
                return False
        else:
            if my_word[index] != other_word[index]:
                return False

    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # remove all white spaces from my_word
    my_word = ''.join(my_word.split())

    flag = False
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            print(word)
            flag = True

    if flag == False:
        print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    # initialize variables
    guesses_left = 6
    warnings = 3
    letters_guessed = []
    while guesses_left != 0 and is_word_guessed(secret_word,letters_guessed) == False:
        print("--------------------------------------------------")
        print("You have " + str(guesses_left) + " guesses left.")
        print("Availabe letters: " + get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ")
        # convert letter to lower so as to handle only lowercase characters
        letter = letter.lower()
        # assuring rule 2
        if letter.isalpha() == False and letter != '*':
            if(warnings != 0):
                warnings = warnings - 1
                print("Oops! That is not a valid letter. You now have " + str(warnings) + " warnings: " + get_guessed_word(secret_word,letters_guessed))
                continue
            else:
                print("Oops! That is not a valid letter: " + get_guessed_word(secret_word,letters_guessed))
                guesses_left = guesses_left - 1
                continue
        # Handle hint variation
        if letter == '*':
            print("Possible word matches are:")
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            show_possible_matches(guessed_word)
            continue
        # assuring rule 3
        if letter not in letters_guessed:
            # append the letter in the list if and only if it has not been added Before
            letters_guessed.append(letter)
        else:
            # user has already guessed this letter
            if(warnings != 0):
                warnings = warnings - 1
                print("Oops! You 've already guessed that letter. You now have " + str(warnings) + " warnings: " + get_guessed_word(secret_word,letters_guessed))
                continue
            else:
                print("Oops! You 've already guessed that letter. You now have no warnings left, so you lose one guess: " + get_guessed_word(secret_word,letters_guessed))
                guesses_left = guesses_left - 1
                continue
        # Check if we have found a letter from the secret_word
        if(is_letter_guessed(secret_word,letter)):
            print("Good guess: " + get_guessed_word(secret_word,letters_guessed))
        else:
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word,letters_guessed))
            # reduce guesses_left by one if is consonant
            if(is_vowel(letter) == False):
                guesses_left = guesses_left - 1
            # reduce guesses_left by two if is vowel
            else:
                guesses_left = guesses_left - 2



    print("-------------")
    if guesses_left == 0:
        print("Sorry, you ran out of guesses. The word was else.")
    else:
        print("Congratulations, you won!")
        total_score = guesses_left * unique_letters_in_word(secret_word)
        print("Your total score for this game is: " + str(total_score))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!

if __name__ == "__main__":

    print("Hello to the Hangman Game!")
    print("Press '1' in order to play the game without hints.")
    print("Press '2' in order to play the game with hints.")

    option = int(input("Your choice: "))
    while(option != 1 and option != 2):
        print("Wrong input! Try again.")
        option = int(input("Your choice: "))

    secret_word = choose_word(wordlist)

    if(option == 1):
        hangman(secret_word)
    elif(option == 2):
        hangman_with_hints(secret_word)
