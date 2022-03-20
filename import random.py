import random
from re import L

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = input('Guess a number between 1 and {x}')
        if guess < random_number:
            print('Guess again, Your number was lower.')
        elif guess > random_number:
            print('Guess again, Your number was too high.')
    
    print(f'You figured it out and it was not that hard, right? The random number was {random_number}')

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c': 
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (H), too low(L) or correct (C)?').lower
        if feedback == 'h':
            high = guess -1
        if feedback == 'l':
            low = guess + + 1
    print(f'Yes, this looks about correct, {guess}, yeah its right!')

    computer_guess(40)