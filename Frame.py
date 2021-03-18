class Frame:
    framesPlayed = 0
    playedTurnValues = []

    def __init__(self, ball_one, ball_two, turnScore):
        self.ballOneScore = ball_one
        self.ballTwoScore = ball_two
        self.turnScore = turnScore
        self.framesPlayed += 1

        self.playedTurnValues = [self.ballOneScore, self.ballTwoScore, self.turnScore]

        Frame.framesPlayed += 1
        # print("New frame added: ", self.playedTurnValues) #Used for Debugging