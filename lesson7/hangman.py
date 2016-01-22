# This is a hangman game.
# Your game must do the following things.
# Everytime a user guesses a character, it should tell them if their character
# is in the secret word or not.
#
# Also, it should print the guessed character in the following format
# if the secret word is unicorn and the user guessed the letter 'n'
# you program should print _n____n
#
# It should also print a picture of the current state of the hanged man.
#
# If the user guesses a letter he already guessed, give them a warning.
#
# The user can make at most 6 mistakes.

import random # don't worry about these lines.
from hangman_pics import HANGMANPICS

LIST_OF_WORDS = ['hangman', 'chairs', 'backpack', 'bodywash', 'clothing', 'computer', 'python', 'program', 'glasses', 'sweatshirt', 'sweatpants', 'mattress', 'friends', 'clocks', 'biology', 'algebra', 'suitcase', 'knives', 'ninjas', 'shampoo']

# First let's write a function to select a random word from the list of words.
def getSecretWord():
  # this line generates a random number use it to index into the list of words
  # and return a secret word.
  rnd = random.randint(0, len(LIST_OF_WORDS) - 1)
  return ...

secret_word = getSecretWord() # functions help us organize our code!
mistakes = 0

# Now create an empty list to keep track of the letters the user guessed

def string_contains_character(c, word):
  # copy your function from lesson6 here.

def hide_word(guesses, secret_word):
  hidden_word = ""
  for letter in secret_word:
    if letter in guesses:
      ...

# This is the
while(True):
  guess = raw_input()
  # Check if the guess was a letter that the user already guessed. If so,
  # give them a warning and go back to the beginning of the loop.

  # If this is a new guess, add it to the list of letters the user guessed.
  # Maybe you could use one of the list methods...

  # Check if the new guess is in the secret word, using the function
  # string_contains_character you wrote on lesson6.
  # If the user made a mistake, increase their number of mistakes and let them
  # know!

  # Now, complete the function hide_word, which takes in the guesses made and
  # the secret_word and returns a the word in a hidden format. Remember, if the
  # letter was in the guesses, it should appear in the word, if it's not it
  # should appear as an underscore "_"
  #
  # If your hidden word has no underscores, the user won! Let them know about
  # that and break out of the loop


  print(HANGMANPICS[mistakes]) # this line will print a picture of the hanged man

  # If the user made 6 mistakes, tell them the game is over and break out of the
  # loop.