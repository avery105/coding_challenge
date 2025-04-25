def board(spots):
    spots = "|1|2|3|\n|4|5|6|\n|7|8|9|"

(f' {spots[1]}|{spots[2]}|{spots[3]}"
        f"|{spots[4]}|{spots[5]}|{spots[6]}\n"
        f"|{spots[7]}|{spots[8]}|{spots[9]}\n")


)


#board="|1|2|3|\n|4|5|6|\n|7|8|9|"
    #   print (board)
# {'1:1 2:2 3:3 4:4 5:5 6:6 7:7 8:8 9:9'}

#board = (f"{spots [1]}|{spots[2]}|{spots [3]}|{spots[3]}|\n")
def check_turn (turn):
    if check_turn % 2 == 0:return '0'
    else:return 'x'
    if turn % 2 == 0:return '0'
    else:return 'x'
def check_win(board):