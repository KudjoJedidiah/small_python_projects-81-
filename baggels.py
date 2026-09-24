"""
A deductive logic game where you must guess a
number based on clues

"""

import random

NUM_DIGITS=3
MAX_GUESSES=10

def main():
    print('''Bagels, a deductive logic game.s

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say: Pico
That means: One digit is correct but in the wrong position.
When I say:Fermi 
That means:One digit is correct and in the right position.
When I say:Bagels 
That means:No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))


    
    while True:
        secretNum=getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it'.format(MAX_GUESSES))

        numGuesses=1
        while numGuesses <=MAX_GUESSES:
            guess= ''
            #Keep looping until they enter a valid guess:
            while len(guess)!=NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess=input('> ')

            clues=getClues(guess,secretNum)
            print(clues)
            numGuesses +=1

            if guess==secretNum:
                break

            if numGuesses>MAX_GUESSES:
                print('You ran out of guesses.')
                print('Your answer was {}'.format(secretNum))

        print('Do you want to play again?(yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    numbers=list('0123456789')
    random.shuffle(numbers)
    secretNum= ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess,secretNum):
    """Returns a string with the pico,fermi,bagels clues for a guess
    and secret number pair."""
    if guess==secretNum:
        return 'You got it'

    clues=[]

    for i in range(len(guess)):
        if guess[i]==secretNum[i]:
            #A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            #A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues)==0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()