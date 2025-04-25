# import os
#-----------------------------------------------------------------------------
# Name: tic-tac-toe       Enhanced New File (enhancedNewFile.py)
# Purpose:   to make the board game tic-tac-toe
#1 make a game
# Author:      Jayden
#
# Created:     23-April-2025
# Updated:     25-April-2025
#----------------------------------------------------------------
# 🔁 Alternates between 'X' and 'O' based on turn number
def check_turn(turn):
    return 'X' if turn % 2 == 0 else 'O'

# ✅ Checks for a win by comparing the board positions
def check_for_win(spots):
    wins = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
        (1, 5, 9), (3, 5, 7)              # Diagonals
    ]
    for a, b, c in wins:
        if spots[a] == spots[b] == spots[c]:
            return True
    return False

# 🎨 Draws the game board to the terminal
def draw_board(spots):
    print(f"\n {spots[1]} | {spots[2]} | {spots[3]}")
    print("---|---|---")
    print(f" {spots[4]} | {spots[5]} | {spots[6]}")
    print("---|---|---")
    print(f" {spots[7]} | {spots[8]} | {spots[9]}\n")

# 🧠 Game state setup
spots = {i: str(i) for i in range(1, 10)}
playing, complete = True, False
turn = 0
prev_turn = -1

# 🎮 Game Loop
while playing:
   # os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn

    print(f"Player {(turn % 2) + 1}'s turn: Pick your spot or press 'q' to quit")
    choice = input()

    if choice.lower() == 'q':
        playing = False
        continue

    if choice.isdigit() and int(choice) in spots:
        spot = int(choice)
        if spots[spot] not in {'X', 'O'}:
            spots[spot] = check_turn(turn)
            turn += 1
    else:
        continue  # Invalid input

    if check_for_win(spots):
        playing, complete = False, True
    elif turn >= 9:
        playing = False

# 🏁 Game over screen and results
# os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

if complete:
    winner = 'Player 1' if check_turn(turn - 1) == 'X' else 'Player 2'
    print(f"{winner} Wins!")
else:
    print("No Winner")

print("Thanks for playing!")
