import random
secretNumber = random.randint(1, 20)
# Let's start a guess the number game

print('Hello! Would you like to play a game with me?')
answer = input()
if answer == 'Yes':
     print('I am  thinking about a number between 1 and 20.')
elif answer == 'No':
    print('No problem. Bye, bye!')


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
