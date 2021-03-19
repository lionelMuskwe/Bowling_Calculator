import time
from Scoreboard import *

class Frame:
    framesPlayedCounter = 0

    def __init__(self, ball_one, ball_two):
        self.ballOneScore = ball_one
        self.ballTwoScore = ball_two
        self.turnScore = ball_one + ball_two
        self.turnType = ""
        self.frameNumber = Frame.framesPlayedCounter

        if ball_one == 10 or ball_two == 10:
            self.turnType = "strike"

        elif self.turnScore == 10:
            self.turnType = "spare"

        else:
            self.turnType = "normal"

        if self.turnType == "spare":
            pass

        if Frame.framesPlayedCounter > 0:
            self.turnScore += Scoreboard.rows[Frame.framesPlayedCounter - 1][2]

        self.playedFrameValues = [self.ballOneScore, self.ballTwoScore, self.turnScore]

        Scoreboard.rows[Frame.framesPlayedCounter] = self.playedFrameValues
        Scoreboard.printScoreBoard(Scoreboard)

        # debugging lines of code
        print("[DEBUG] Frame Counter :", Frame.framesPlayedCounter)
        print("[DEBUG] ScoreboardFrames :", Scoreboard.rows)

        Frame.framesPlayedCounter += 1  # registed as a played frame
        # print("New frame added: ", self.playedTurnValues) #Used for Debugging

