# first import randint for Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
from random import randint

#make a function for write in OOP form
def Guess_Number(x):
    create_numner = randint(1, x)
    guess = 0 # Define our guess
    while guess != create_numner: # a loop that try to guess my mind with ask and answer
        guess = int(input(f"Guess a number in 1 to {x} : "))
        if guess < create_numner : print("ops,guess again. its too low!!")
        elif guess > create_numner : print("ops,guess again. its too hight!!")

    print(f"yesss.you have guessed the number {guess} correctly!!") # when you pass the loop this code will run to say OK to you

Guess_Number(10)

