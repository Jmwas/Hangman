# Word guessing game based on hangman
import random
from dictionary import dict

tries = 0
wrong = []

word = random.choice(dict)
print(word)

while True:
    question = input("Do you want to continue? Y/N: ")
    question.lower()

    if question not in ('y', 'n'):
        print("Please select y or n")

    elif question == 'y':
        word_length = len(word)
        print('You have %2d tries' % (len(word)))

        while tries < word_length:
            a = input("Please guess a letter: ")

            if a in word:
                print('%s is in the word' % a)
                word = word.replace(a, '')
                print(word)
            else:
                print('wrong, %s is not in the word' % a)
                wrong.append('X')
                tries += 1
            print(tries, len(word))
        print(word)
    break
