import time
from Scoreboard import *
import click


class Frame:
    framesPlayedCounter = 0  # keeps track of the number of frames created/ instanced
    savedPlayedFrames = []  # all the Frames are stored as classes in this file

    def __init__(self, ball_one, ball_two):
        self.ballOneScore = ball_one
        self.ballTwoScore = ball_two
        self.turnScore = ball_one + ball_two
        self.framePosition = Frame.framesPlayedCounter

        if ball_one == 10 or ball_two == 10:
            self.turnType = "strike"

        elif self.turnScore == 10:
            self.turnType = "spare"

        else:
            self.turnType = "normal"

        self.playedFrameValues = [self.ballOneScore, self.ballTwoScore, self.turnScore] # array of Frame values
        Frame.savedPlayedFrames.append(self)
        Scoreboard.rows[Frame.framesPlayedCounter] = self.playedFrameValues

        Frame.framesPlayedCounter += 1  # registed as a played frame

        # checking if the last frame was a strike or spare.
        # It only runs, when on Frame 2 and above
        if Frame.framesPlayedCounter > 1:
            if Frame.savedPlayedFrames[self.framePosition - 1].turnType == "strike":
                self.lastballWasStrike()
                Frame.sendValuesToScoreboard(Frame.savedPlayedFrames)

            elif Frame.savedPlayedFrames[self.framePosition - 1].turnType == "spare":
                self.lastballWasSpare()
                Frame.sendValuesToScoreboard(Frame.savedPlayedFrames)

        Frame.getTotalScore(self, Frame.savedPlayedFrames)
        click.clear()
        Scoreboard.printScoreBoard(Scoreboard)  # calls the print Scoreboard function found in the Scoreboard class


    # the code below handles strikes and spares
    def updateScoreboard(self):
        Scoreboard.rows[self.framePosition] = self.playedFrameValues

    def lastballWasStrike(self):  # runs if last ball was a spare
        Frame.savedPlayedFrames[self.framePosition - 1].turnScore += self.ballOneScore  # this is where the extra value is being added

        if self.ballOneScore < 10:
            Frame.savedPlayedFrames[self.framePosition - 1].turnScore += self.ballTwoScore  # adding the second ball

    def lastballWasSpare(self): # runs if last ball was a spare
        Frame.savedPlayedFrames[self.framePosition - 1].turnScore += self.ballOneScore  # this is where the extra value is being added

    def sendValuesToScoreboard(allFrames):  # updates the values on the scoreboard, after each frame ends
        for i in allFrames:
            i.updateScoreboard()

    def getTotalScore(self, allFrames):
        # this function, loops all played frames then using a running variable, it begins to assigning values to the
        # third position "playedFrameValues[]" dynamically

        Scoreboard.totalScore = 0
        if Frame.framesPlayedCounter > 0:
            for i in allFrames:
                frameScore = i.turnScore
                Scoreboard.totalScore += frameScore
                self.playedFrameValues[2] = Scoreboard.totalScore
        else:
            Scoreboard.totalScore = allFrames[0].turnScore
            self.playedFrameValues[2] = Scoreboard.totalScore