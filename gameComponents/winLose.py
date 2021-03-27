from gameComponents import gameVars

def winorlose(status):
    if status == "won":
        print = "You must be a god of some sorts... There is no way mere human can defeat the likes of AI!"
    else:
        print = "AI is just far superior in comparison to the human mind. Don't be ashamed of your lost. "

    print(pre_message + 'Play again?')

    choice = False

    while choice == False:
        choice = input("Y / N? ")

        if choice == "Y" or choice == "y":
            gameVars.player_lives = gameVars.total_lives
            gameVars.computer_lives = gameVars.total_lives
            gameVars.player_choice = False

        elif choice == "N" or choice == "n":
            print("You chose to quit.")
            exit()

        else:
            print("Make a valid choice - Y or N")
            choice = False