
size = 5
board = ""

for y in range (0,size,1):
    for x in range (0,size,1):
        if (x + y) % 2 == 0:
            board += " "
        else:
            board += "#"

    board += "\n"


print(board)
