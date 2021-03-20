import time
from Scoreboard import *

class Frame:
    framesPlayedCounter = 0
    savedPlayedFrames = []

    def __init__(self, ball_one, ball_two):
        self.ballOneScore = ball_one
        self.ballTwoScore = ball_two
        self.turnScore = ball_one + ball_two
        self.turnType = ""
        self.framePosition = Frame.framesPlayedCounter

        if ball_one == 10 or ball_two == 10:
            self.turnType = "strike"

        elif self.turnScore == 10:
            self.turnType = "spare"

        else:
            self.turnType = "normal"

        if Frame.framesPlayedCounter > 1:
            self.turnScore += Scoreboard.rows[Frame.framesPlayedCounter - 1][2]


        self.playedFrameValues = [self.ballOneScore, self.ballTwoScore, self.turnScore]
        Frame.savedPlayedFrames.append(self)
        Scoreboard.rows[Frame.framesPlayedCounter] = self.playedFrameValues
        Scoreboard.printScoreBoard(Scoreboard)

        # debugging lines of code
        # print("\t\t[DEBUG] Frame Counter    :", Frame.framesPlayedCounter)
        # print("\t\t[DEBUG] ScoreboardFrames :", Scoreboard.rows)

        Frame.framesPlayedCounter += 1  # registed as a played frame
        # print("New frame added: ", self.playedTurnValues) #Used for Debugging

        #checking if the last frame was a strike
        if Frame.framesPlayedCounter > 0:

            if Frame.savedPlayedFrames[self.framePosition - 1].turnType == "strike":
                print("Last frame was a strike")
                self.lastballWasStrike()
                Frame.sendValuesToScoreboard(Frame.savedPlayedFrames)

            elif Frame.savedPlayedFrames[self.framePosition - 1].turnType == "spare":
                print("Last frame was a spare")
                self.lastballWasSpare()
                Frame.sendValuesToScoreboard(Frame.savedPlayedFrames)


            else:
                print("Might have been a normal frame")


    def updateScoreboard(self):
        Scoreboard.rows[self.framePosition] = self.playedFrameValues

    def lastballWasStrike(self):
        print("---Updating  Scoreboard with new values")
        Frame.savedPlayedFrames[self.framePosition - 1].playedFrameValues[2] += self.ballOneScore  # this is where the extra value is being added
        print("---Done changing new values")

        if self.ballOneScore < 10:
            Frame.savedPlayedFrames[self.framePosition - 1].playedFrameValues[2] += self.ballTwoScore  # adding the second ball
            print("---Second ball value added")

    def lastballWasSpare(self):
        print("---Updating  Scoreboard with new values")
        Frame.savedPlayedFrames[self.framePosition - 1].playedFrameValues[2] += self.ballOneScore  # this is where the extra value is being added
        print("---Spare score added")


    def sendValuesToScoreboard(allFrames):
        for i in allFrames:
            i.updateScoreboard()
        Scoreboard.printScoreBoard(Scoreboard)