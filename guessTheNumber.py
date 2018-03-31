print('Hello! Would you like to play a game with me?')
# Let's start a guess the number game
import random
secretNumber = random.randint(1, 20)
print('I am  thinking about a number between 1 and 20.')

#Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # Here is the correct value

if guess == secretNumber:
    print('You win! Good job!')
else:
    print('No. The right number is ' + str(guessesTaken) .)
