from random import randint
from gameComponents import gameVars, winLose

while gameVars.player_choice is False:
    print("============*/ Hello, welcome to my Rock, Paper, Scissors game! */=============")
    print("My name is Aaron Isco, also known as AI. My chances of victory are certain. BOL")
    print("===============================================================================")
    print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("====================================================")

    print("Type out your choice as it will be your last, or type quit to admit defeat\n")
    gameVars.player_choice = input("Choose rock, paper, or scissors: \n")

    if gameVars.player_choice == "quit":
        print("Choosing to quit? My victory was always inevitable. Have a nice day")
        exit()

    print ("==============================================================================")
    gameVars.computer_choice = gameVars.choices[randint(0, 2)]

    print("user chose: " + gameVars.player_choice)
    print("computer chose: " + gameVars.computer_choice)

    if gameVars.computer_choice == gameVars.player_choice:
        print("The round has ended in a draw")
    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            gameVars.player_lives -= 1
            print("Your lost was inevitable. Here are your remaining lives:", gameVars.player_lives)
        else:
            print("I lost...? My code must be malfunctioning.")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "rock":
            gameVars.player_lives -= 1
            print("AI remains victorious as scripted. Here are your remaining lives:", gameVars.player_lives)
        else:
            print("This can not be, AI can not possibly lose!")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
            gameVars.player_lives -= 1
            print("You should have quit when you had the chance. Here are your remaining lives:", gameVars.player_lives)
        else:
            print("AI does not compute with losing, my circuits must be under attack")
            gameVars.computer_lives -= 1

    if gameVars.player_lives == 0:
        winLose.winorlose("AI is superior. You were always bound to lose. Thank you for playing :)")
    elif gameVars.computer_lives == 0:
        winLose.winorlose("I lost? There must be some bugs in the code. We shall play again once I have been debugged by my master.")
    else:
        gameVars.player_choice = False
