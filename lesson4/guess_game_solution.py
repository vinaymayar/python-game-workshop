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

MAX_NUMBER_OF_GUESSES = 10 # it's good practice to assign constant values to
                           # variables names entirely capitalized
tentative = 0
while(True): # don't worry about this either, but be sure to follow the indentation level
    print("Make your guess:")
    guess = input() # remember how we get the input from the user?
    if (guess == secret_number):
        # add a print statement letting the user know they made the right guess.
        print("You guessed the correct number!")

        break; # don't worry about this line, we will learn more about this, when we
               # learn about loops!

    elif guess > secret_number: # how can we check if the guess is too high?
        # what should we do if the guess is too high?
        print("The number is too high!")

    else:
        # what should we do if the guess is too low?
        print("The number is too low!")

    tentative += 1
    if tentative > MAX_NUMBER_OF_GUESSES:
        print("You ran out of guesses and lost the game!")
        break;
