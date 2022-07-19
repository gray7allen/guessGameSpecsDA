"""A number-guessing game."""

from random import randint

tries = 0
number = randint(1, 100)

print('Hi, what\'s your name?')

name = input('(type in your name) ')

print(f'{name}, I\'m thinking of a number between 1 and 100.')
print('Can you guess what the number is?')

while True:
    guess = input('Your guess? ')

    try:
        guess = int(guess)
    except ValueError:
        print(f'"{guess}" is not a valid number, try again.')
        continue

    if guess < 1 and guess > 100:
        print('Please guess a number between 1 and 100')
        continue

    tries += 1

    if guess < number:
        print('Your guess is too low, try again.')

    elif guess > number:
        print('Your guess is too high, try again.')

    else:
        print(f'Well done, {name}!')
        print(f'You found my number in {tries} tries!')
        break