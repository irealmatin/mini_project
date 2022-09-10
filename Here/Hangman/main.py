import random
import string

from words import words


# Define a function for get valid words . otherwise that word wich have not space and dashes in middle of them
def valid_word(words):
    get_word = random.choice(words)
    while '-' in get_word or ' ' in get_word:
        get_word = random.choice(words)

    return get_word.upper()

def Hangman():
    get_word = valid_word(words)
    word_letters = set(get_word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    live = 7

    while len(word_letters) > 0 and live > 0 :
        # corrent status
        print('You have', live , 'lives left and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in get_word]
        print('Current words --->  ', ' '.join(word_list)) # change this ['-', '-', '-', '-', '-', '-', '-', '-'] to this --------

        user_letter = input('type your Guess please: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                live = live - 1  # dicrease life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters: print('\nYou have already used that letter. Guess another letter')
        else : print('its not valid')


        if live == 0: # get a message to show you could not guess the word correctly
            print('#' * 100)
            print('#' * 99)
            print('#' * 98)
            print('You died, sorry babe :))))) . The word was', get_word)
        else:
            print('#' * 100)
            print('#' * 99)
            print('#' * 98)
            print('wooow! You guessed the word', get_word, 'correctly')
        

if __name__ == '__main__':
    Hangman()
