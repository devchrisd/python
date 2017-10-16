# Guess my number
import random

guessesTaken = 0

print("Hello! What's your name?")
name = input()

number = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1
    
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses! ^_^')
        break

    if guess < number:
        print ('Your guess is too low. :(')

    if guess > number:
        print('Your guess is too high. :-(')

if guess != number:
    number = str(number)
    print ('Nope. The number I was thinking of was ' + number)
