from Scoreboard import *
from Frame import *

newScoreboard = Scoreboard()

def rollTurn():
    if Frame.framesPlayedCounter <= 9:
        print("\n\tFrame Number {0}".format(Frame.framesPlayedCounter + 1))  # adds to static variable which tracks number of frames played
        while True:
            ball_one = input("\tBall [1] pins knocked down :")
            if ball_one.isdigit():
                ball_one = int(ball_one)
                if ball_one <= 10:
                    break
                else:
                    print("You can't drop more that 10 pins in one go")
            else:
                print("Invalid Input, please enter a valid integer")

        while True:
            if ball_one != 10: # if first ball is 10 then second ball input is not required
                ball_two = input("\tBall [2] pins knocked down :")
                if ball_two.isdigit():
                    ball_two = int(ball_two)
                    break
                else:
                    print("Invalid Input, please enter a valid integer")
            else:
                ball_two = 0
                break

        if ball_one + ball_two > 10:
            print("To many pins were knocked down!")
            print("Try enter the correct values")
            rollTurn()

        else:
            Frame(ball_one, ball_two)

    else:
        print("All 10 frames have been played")
        input("Press anything to exit")  # stops program from closing after completion
        exit()


newScoreboard.printScoreBoard()  # this prints the first scoreboard with all zeroes

while True:
    rollTurn()