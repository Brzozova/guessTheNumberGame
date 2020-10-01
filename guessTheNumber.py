
 # GUESS THE NUMBER GAME ( MULTIPLAYER GAME WITH SPEAKING FUNCTIONALITY )

# hey buddy, please tell me how is this version of this game?

import random

from win32com.client import Dispatch





def speak(str):

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)



trails_taken = 0  # initialising the no of trials

trails_taken1 = 0



speak("Welcome to the guess the number game")

speak("Please enter the name of the respective players...")

player1 = input("Please enter the name of Player 1\n")

player2 = input("Please enter the name of player 2\n")

speak("Please enter the range in which you wanna to guess the number")

a = int(input("Please enter the value of starting range\n"))

b = int(input("Please enter the value of last range\n"))



# creating a random digit which users have to find

preciousWord = random.randrange(a+1, b)

speak(f"I have generated a number between {a} and {b}.")



# inputs of player 1 

while True:

    print(f"Its {player1}'s turn")

    _input = int(input(f"{player1},  please enter the number\n"))

    trails_taken +=1

    

    if _input > preciousWord:

        print(f"{player1} entered: {_input}")

        speak("Guess a lesser value")

        print("Wrong guess....")    

        print("Please enter a lesser value")    

        # trails_taken += 1

        print(f"Trials taken {trails_taken}")

        print("--------------------------------------------------------")



        

    elif _input < preciousWord:

        print(f"{player1} entered: {_input}")

        print("Wrong guess")

        speak("Guess a higher value")

        print("Please enter a larger value")

        # trails_taken += 1

        print(f"Trials taken {trails_taken}")

        print("--------------------------------------------------------")



    elif _input == preciousWord:

        print(f"{player1} entered: {_input}")

        print(f"Congrates! You won. Correct number was {preciousWord}")

        speak(f"Congratulations {player1}, you have found the number ")

        print(f"Trials taken {trails_taken}")

        print("--------------------------------------------------------")

        break

    

# player2's inputs

while True:

    

    print(f"Its {player2}'s turn")

    _input1 = int(input(f"{player2},  please enter the number\n"))

    trails_taken1 += 1

    

    if _input1 > preciousWord: 

        print(f"{player2} entered: {_input1}")

        print("Wrong guess....")    

        speak("Guess a lesser value")

        print("Please enter a lesser value")    

        # trails_taken1 += 1

        print(f"Trials taken {trails_taken1}")

        print("--------------------------------------------------------")



        

    elif _input1 < preciousWord:

        print(f"{player2} entered: {_input1}")

        print("Wrong guess")

        speak("Guess a higher value")

        print("Please enter a larger value")

        # trails_taken1 += 1

        print(f"Trials taken {trails_taken1}")

        print("--------------------------------------------------------")



    elif _input1 == preciousWord:

        print(f"{player2} entered: {_input1}")

        print(f"Congrates! You won. Correct number was {preciousWord}")

        speak(f"Congratulations {player2}, you have found the number ")

        print(f"Trials taken {trails_taken1}")

        print("--------------------------------------------------------")

        break

    

# results

if trails_taken > trails_taken1:

    speak(f"{player1} taken {trails_taken} trails and {player2} taken {trails_taken1} trails")

    print(f"{player1} taken {trails_taken} trails and {player2} taken {trails_taken1} trails")

    speak(f"Hence {player2} won this match!")

    print(f"Hence {player2} won this match!")

    speak("Hope You enjoyed the game...")



elif trails_taken1 > trails_taken:

    speak(f"{player1} taken {trails_taken} trails and {player2} taken {trails_taken1} trails")

    print(f"{player2} taken {trails_taken1} trails and {player1} taken {trails_taken} trails")

    speak(f"Hence {player1} won this match!")

    print(f"Hence {player1} won this match!")

    speak("Hope You enjoyed the game....")



elif trails_taken == trails_taken1:

    speak(f"{player1} taken {trails_taken} trails and {player2} has also taken {trails_taken1} trails")

    print(f"{player2} taken {trails_taken1} trails and {player1} taken {trails_taken} trails")

    speak("Hence this match is tied!")

    print(f"Hence this match is tied!")

    speak("Hope You enjoyed the game")
