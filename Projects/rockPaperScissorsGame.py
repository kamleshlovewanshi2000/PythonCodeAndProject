import random

l = ["Rock", "Scissor", "Paper"]

'''
Conditions:
     User  Computer
      |       |
    Rock vs Paper -> Paper Wins           if (user == "Rock" and computer == "Paper") ==> Computer Winner  : Computer Fold the Rock by using Paper
    Rock vs Scissor -> Rock Wins          if (user == "Rock" and computer == "Scissor") ==> User Winner    : Rock brack the Scissor 
    Paper vs Scissor -> Scissor Wins      if (user == "Paper" and computer == "Scissor") ==> Computer Winner : Because Scissor cuts the Paper
'''

while True:
    ccount = 0
    ucount = 0
    uchoice = int(input('''
    Game Start ...
    1: Yes
    2: Exit Game
    '''))
    if uchoice == 1:
        # pass
        for i in range(1, 6):             # There are Five Rounds in this game
            # Taking the User Input
            userInput = int(input('''
            1: Rock
            2: Scissor
            3: Paper
            '''))
            # Takes user Choice
            if userInput == 1:
                userChoice = "Rock"
            elif userInput == 2:
                userChoice = "Scissor"
            elif userInput == 3:
                userChoice = "Paper"

            # Takes Computer Choice
            computerChoice = random.choice(l)

            # Condition for Game Draw
            if userChoice == computerChoice:
                print("User Choice:", userChoice)
                print("Computer Choice:", computerChoice)
                print("Game is Draw ...!")
                # ucount += 1
                # ccount += 1

            # Condition for User Wins
            elif (userChoice == "Rock" and computerChoice == "Scissor") or (
                    userChoice == "Paper" and computerChoice == "Rock") or (
                    userChoice == "Scissor" and computerChoice == "Paper"):
                print("User Choice:", userChoice)
                print("Computer Choice:", computerChoice)
                print("You Wins ...!")
                ucount += 1

            # Condition for Computer wins
            else:
                print("User Choice:", userChoice)
                print("Computer Choice:", computerChoice)
                print("Computer Wins ...!")
                ccount += 1

        print()
        print("<--------------***....Final Result....***------------->")
        # Final Result Code
        # Condition: final User Winner
        if ucount > ccount:
            print("Your Winner ... 😊 ✌ !")
            print("Your Count :", ucount)
            print("Computer Count :", ccount)
        # Condition: Final match is Draw
        elif ucount == ccount:
            print("Match is Draw ... 😐 !")
            print("Your Count :", ucount)
            print("Computer Count :", ccount)
        # Condition: Final Computer Winner
        else:
            print("Computer Winner ... 😊 ✌ !")
            print("Computer Count :", ccount)
            print("Your Count :", ucount)


    else:
        print("Game is Over...")
        break
