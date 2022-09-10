# first import randint for Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
from random import randint

#make a function for write in OOP form
def computer_guess(x):
    min_g = 1 # Lower number than can choose
    max_g = x # last number
    result = "" 
    while result != 'c':
        if min_g != max_g : guess = randint(min_g,max_g) # run when guess is not 1
        else : guess = min_g # if answer is 1 . x = y ,  1 = 1
        result = input(f"is {guess} too high(h) , too low(l) or correct(c) ?  ").lower()
        if result == 'h': 
            max_g = guess - 1
        if result == 'l':
            min_g = guess + 1
    
    print(f"wow . I can guessed the number {guess} correctly")

computer_guess(20) # optional value
