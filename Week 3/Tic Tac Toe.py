
# Building Board
boardSize = int(input("Please input board size: "))


def printhorizontalline():
    print(" --- " * boardSize)


def printverticalline():
    print("|    " * (boardSize + 1))

for index in range(boardSize):
    printhorizontalline()
    printverticalline()
    printhorizontalline()


# Checking if game has been won.
# 0 means nobody has played space
# 1 means player 1 has played space
# 2 means player has played space

game = [[], [], []]

if game = ([[0], [], []]) :