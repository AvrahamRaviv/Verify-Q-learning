from Class import State, Player
from utils import InitToNumbers, createVecs, writeSmv, INIT, BOARD_ROWS
from datetime import datetime, timedelta

expRate = 0
max_turn = 50
NumOfIteration = 1


if __name__ == "__main__":

    Results = []
    Runtime = []
    for i in range(NumOfIteration):
        now = datetime.now()
        start = 0
        stop = 0
        max_games = 15000
        numOfPlayers = int(len(InitToNumbers(ret_type=str)) / 2)  # Number of players derive from initial vector
        expRate = 0.3  # rate [ 0-1 ] the agent explore new action without leaning on Q-table
        pl1 = Player("p1", exp_rate=expRate)  # create first Player class (Class.py)
        pl2 = Player("p2", exp_rate=expRate)  # create second Player class (Class.py)
        st = State(INIT, pl1, pl2, max_turn)  # create new variable, st, in form of State class (Class.py)
        a_v, l_v = createVecs(numOfPlayers, BOARD_ROWS - 1)  # a_v - full list of possible state vectors
                                                             # l_v - shorter list with group of vectors that span the board dimensions
        res = st.play(max_games, INIT, a_v, l_v, numOfPlayers)
        print(res)
        print("Number of games:", sum(res))
        current_time = now.strftime("%H:%M:%S")
        Results.append(current_time)
        Results.append(res)
        # save runtime
        stop = datetime.now()
        runtime_game = float((stop - now).total_seconds())  # save runtime in seconds
        Runtime.append(runtime_game)

    print(Results)
    print(Runtime)
    fname = '1_03042021_Results_One_Cop_BR5_RANDOM_False.txt'
    with open(fname, 'w') as fw:
        for item in Results:
            fw.write("%s\n" % item)
        for item in Runtime:
            fw.write("%s\n" % item)

