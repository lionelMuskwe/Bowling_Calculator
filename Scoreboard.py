class Scoreboard:
    rows = []

    def __init__(self):
        for i in range(10):
            self.rows.append([0, 0, 0])



    def printScoreBoard(self):
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t| FRAME # ||  BALL #1  |  BALL #2  ||   Score   |")
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    1    ||     {0}     |     {1}     ||     {2}     |".format(self.rows[0][0], self.rows[0][1], self.rows[0][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    2    ||     {0}     |     {1}     ||     {2}     |".format(self.rows[1][0], self.rows[1][1], self.rows[1][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    3    ||     {0}     |     {1}     ||     {2}     |".format(self.rows[2][0], self.rows[2][1], self.rows[2][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    4    ||     {0}     |     {1}     ||     {2}     |".format(self.rows[3][0], self.rows[3][1], self.rows[3][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    5    ||     {0}     |     {1}     ||     {2}     |".format(self.rows[4][0], self.rows[4][1], self.rows[4][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    6    ||     {0}     |     {1}     ||     {2}     |".format(self.rows[5][0], self.rows[5][1], self.rows[5][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    7    ||     {0}     |     {1}     ||     {2}     |".format(self.rows[6][0], self.rows[6][1], self.rows[6][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    8    ||     {0}     |     {1}     ||     {2}     |".format(self.rows[7][0], self.rows[7][1], self.rows[7][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    9    ||     {0}     |     {1}     ||     {2}     |".format(self.rows[8][0], self.rows[8][1], self.rows[8][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    10   ||     {0}     |     {1}     ||     {2}     |".format(self.rows[9][0], self.rows[9][1], self.rows[9][2]))
        print("\t\t----------||-----------|-----------||------------")


