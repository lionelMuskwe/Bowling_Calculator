class Scoreboard:
    rows = []  # holds the arrays appended within the Frame class per each instance.
    totalScore = 0  # used in conjunction with the Frame class, "getTotalScore" function

    def __init__(self):
        for i in range(10):  # sets the initial scoreboard to begin with zeros only
            Scoreboard.rows.append([0, 0, 0])

    def printScoreBoard(Scoreboard):
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t| FRAME # ||  BALL #1  |  BALL #2  ||   Score   |")
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    1    ||     {0}     |     {1}     ||     {2}     ".format(Scoreboard.rows[0][0], Scoreboard.rows[0][1], Scoreboard.rows[0][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    2    ||     {0}     |     {1}     ||     {2}     ".format(Scoreboard.rows[1][0], Scoreboard.rows[1][1], Scoreboard.rows[1][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    3    ||     {0}     |     {1}     ||     {2}     ".format(Scoreboard.rows[2][0], Scoreboard.rows[2][1], Scoreboard.rows[2][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    4    ||     {0}     |     {1}     ||     {2}     ".format(Scoreboard.rows[3][0], Scoreboard.rows[3][1], Scoreboard.rows[3][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    5    ||     {0}     |     {1}     ||     {2}     ".format(Scoreboard.rows[4][0], Scoreboard.rows[4][1], Scoreboard.rows[4][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    6    ||     {0}     |     {1}     ||     {2}     ".format(Scoreboard.rows[5][0], Scoreboard.rows[5][1], Scoreboard.rows[5][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    7    ||     {0}     |     {1}     ||     {2}     ".format(Scoreboard.rows[6][0], Scoreboard.rows[6][1], Scoreboard.rows[6][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    8    ||     {0}     |     {1}     ||     {2}     ".format(Scoreboard.rows[7][0], Scoreboard.rows[7][1], Scoreboard.rows[7][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    9    ||     {0}     |     {1}     ||     {2}     ".format(Scoreboard.rows[8][0], Scoreboard.rows[8][1], Scoreboard.rows[8][2]))
        print("\t\t----------||-----------|-----------||------------")
        print("\t\t|    10   ||     {0}     |     {1}     ||     {2}     ".format(Scoreboard.rows[9][0], Scoreboard.rows[9][1], Scoreboard.rows[9][2]))
        print("\t\t----------||-----------|-----------||------------")