# Challenge: guess-number game infinite number of guesses
# The game: Guess the number game.
# In this game we will try to guess a random number between 0 and 100 generated
# by the computer. Depending on our guess, the computer will give us hints,
# whether we guessed too high, too low or if we guessed correctly.
#
# Challenge: Make the game harder by limiting the number of guesses the player
# can make.
# Hint: Try creating a new variable that counts the number of guesses.
# Increment it every time the user makes a guess and use control flow statements
# to see if they reached the limit!

# Don't worry about these lines.
from random import randint
secret_number = randint(0, 100)

while(True): # don't worry about this either, but be sure to follow the indetation
  print("Make your guess:")
  guess = # remember how we get the input from the user?
  if (guess == secret_number):
    # add a print statement letting the user know he made the right guess.
    break; # don't worry about this line, we will learn more about this, when we
           # learn about loops!

  # what should happen if their guess is too high?
  # what should happen if their guess is too low?


