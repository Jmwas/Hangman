"""
Word guessing game based on hangman.
You get seven tries to guess a letter.
"""

import random
from dictionary import dict

while True:
    question = input("Do you want to continue? Y/N: ")
    question.lower()

    if question not in ('y', 'n'):
        print("Please select y or n")
        continue

    elif question == 'y':
        word = random.choice(dict)
        word1 = word
        tries = 7
        choice = ''
        print('You have %s tries' % tries)

        while tries != 0 and word1 != '':
            a = input("Please guess a letter: ")

            if a in word1:
                print('%s is in the word' % a)
                word1 = word1.replace(a, '')
                choice += str(a)
            else:
                print('wrong, %s is not in the word' % a)
                choice += str(a)
                tries -= 1
            print('you have %s tries remaining' % tries)

        if word1 == '':
            print('\nGame over. You win!! \nThe word is %s \nYou choice letters are %s' % (word, choice))
        else:
            print('\nGame over. You lose!! \nThe word is %s \nYou choice letters are %s' % (word, choice))

    break
