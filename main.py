from Scoreboard import *
from Frame import *

newScoreboard = Scoreboard()

# newScoreboard.printScoreBoard()

def rollTurn():
    if Frame.framesPlayed <= 9:
        print("Frame Number {0}".format(Frame.framesPlayed + 1)) # adds to static variable which tracks number of frames played
        while True:
            ball_one = input("Ball [1] pins knocked down :")
            if ball_one.isdigit():
                ball_one = int(ball_one)
                break
            else:
                print("Invalid Input, please enter a valid integer")

        while True:
            ball_two = input("Ball [2] pins knocked down :")
            if ball_two.isdigit():
                ball_two = int(ball_two)
                break
            else:
                print("Invalid Input, please enter a valid integer")

        if ball_one + ball_two > 10:
            print("To many pins were knocked down!")
            print("Try enter the correct values")
            rollTurn()

        else:
            Frame(ball_one, ball_two, ball_one + ball_two)
            newFrame = [ball_one, ball_two, ball_one + ball_two]
            newScoreboard.rows[Frame.framesPlayed-1] = newFrame
            newScoreboard.printScoreBoard()
    else:
        print("All 10 frames have been played")
        exit()





while True:
    rollTurn()