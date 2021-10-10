#Brian Clark
#20 Oct 18
#Rock Paper Scissors Lizard Spock take 1

#if ran in IDLE don't forget to stretch the screen!

import random

def chance():
    """This will be for the RPSLS roll options"""
    r = random.randint(1,5)
    if r == 1:
        return "Rock"
    elif r == 2:
        return "Paper"
    elif r == 3:
        return "Scissors"
    elif r == 4:
        return "Lizard"
    else:
        return "Spock"

def determine_winner(player, computer):
    global player_win, computer_win
    if player == computer:
        return "We have reached an illogical impasse."
    elif player == "Scissors" and computer == "Paper":
        player_win += 1
        return "Scissors shreds Paper with extreme prejudice."
    elif player == "Paper" and computer == "Rock":
        player_win += 1
        return "Paper covers Rock, as Rock is not worthy of being seen."
    elif player == "Rock" and computer == "Lizard":
        player_win += 1
        return "Rock crushes Lizard. Ew."
    elif player == "Lizard" and computer == "Spock":
        player_win += 1
        return "Lizard poisons Spock. Spock calculates his odds of survival: 0%."
    elif player == "Spock" and computer == "Scissors":
        player_win += 1
        return "Spock smashes Scissors with Vulcan Scissor Smash. It's a thing."
    elif player == "Scissors" and computer == "Lizard":
        player_win += 1
        return "Scissors decapitates Lizard. That's no way for a lizard to get a head."
    elif player == "Lizard" and computer == "Paper":
        player_win += 1
        return "Lizard eats Paper. Pulp Fiction."
    elif player == "Paper" and computer == "Spock":
        player_win += 1
        return "Paper disproves Spock with it's intense and ancient knowledge."
    elif player == "Spock" and computer == "Rock":
        player_win += 1
        return "Spock illogically vaporizes Rock with logic."
    elif player == "Rock" and computer == "Scissors":
        player_win += 1
        return "And as it always has, Rock crushes Scissors."
    elif computer == player:
        return "We have reached an illogical impasse yet again."
    elif computer == "Scissors" and player == "Paper":
        computer_win += 1
        return "Scissors cuts Paper, but more methodically."
    elif computer == "Paper" and player == "Rock":
        computer_win += 1
        return "Paper covers Rock like a newspaper article."
    elif computer == "Rock" and player == "Lizard":
        computer_win += 1
        return "Rock crushes Lizard. Clean-up on aisle 3."
    elif computer == "Lizard" and player == "Spock":
        computer_win += 1
        return "Lizard poisons Spock. Spock is not delicious, but he is dead."
    elif computer == "Spock" and player == "Scissors":
        computer_win += 1
        return "Spock smashes Scissors. This still makes no sense!?"
    elif computer == "Scissors" and player == "Lizard":
        computer_win += 1
        return "Scissors decapitates Lizard. We're going to need a new lizard."
    elif computer == "Lizard" and player == "Paper":
        computer_win += 1
        return "Lizard eats Paper. Gets paper cut on tongue. Survives the day."
    elif computer == "Paper" and player == "Spock":
        computer_win += 1
        return "Paper disproves Spock with it's intense and ancient knowledge."
    elif computer == "Spock" and player == "Rock":
        computer_win += 1
        return "Spock vaporizes Rock with his obscene and condescending gaze."
    elif computer == "Rock" and player == "Scissors":
        computer_win += 1
        return "And as it always has, Rock crushes Scissors."
    else:
        print("That was an illogical entry.")

options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
user_option = None
response = "y"
playagain = None
choice = None
player_win = 0
computer_win = 0

while response.lower() == "y":
    choice = input("Would you like to have the highly superior computer " \
                   + "choose for you? (y/n) ")
    if choice == "n":
        print("\nYou have chosen to determine your own fate. This was likely " \
              + "a mistake. Choose wisely. Your weapons of choice are: ",end=" ")
        print(", ".join(options))#had to look this up on stack, wasn't working...
        print()         #...like print(options,end=" "), kept printing multiple times
        user_option = input("Make your selection: ")
        print()
        computer = chance()
        result = "Player chose: " + user_option + "\t\tComputer chose: " \
                 + computer
        player = user_option
        winner = determine_winner(player, computer)
        score = "Player's Score: " + str(player_win) + "       " + "Computer's " \
                + "Score: " + str(computer_win)
        print()
        print("One, two, three, GO!\n".center(80," "))
        print(result.center(68," "))
        print()
        print(winner.center(80," "))
        print()
        print(score.center(80," "))
        print("\n"*3)
        playagain = input("Would you like to play again? (y/n) ")
        if playagain == "y":
            continue
        else:
            break
    elif choice == "y":
        player = chance()
        computer = chance()
        result = "Player chose: " + player + "\t\tComputer chose: " + computer
        winner = determine_winner(player, computer)
        score = "Player's Score: " + str(player_win) + "       " + "Computer's " \
                + "Score: " + str(computer_win)
        print()
        print("One, two, three, GO!\n".center(80," "))
        
        print(result.center(68," "))
        print()
        print(winner.center(80," "))
        print()
        print(score.center(80," "))
        print("\n"*3)
        playagain = input("Would you like to play again? (y/n) ")
        if playagain == "y":
            continue
        else:
            break
    else:
        print("That is not a valid entry")
        continue
      

#end
print("\n\nThe final score is human:" + str(player_win) + ", computer:" \
      + str(computer_win) + ".")
print()
if player_win > computer_win:
    print("You have achieved the superiority you have always sought.")
elif player_win == computer_win:
    print("The future of our two civilizations must be determined in " \
          + "some other form of combat.")
else:
    print("As expected, the computer has bested humanity for the first time once " \
          + "again.")
input("\n\nThanks for playing! Press Enter to exit the game.")













                   

