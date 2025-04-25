






import os
from second_try_game_helper import check_turn, check_for_win, draw_board

# Declare all the variables we're going to need
spots = {i: str(i) for i in range(1, 10)}
playing, complete = True, False
turn = 0
prev_turn = -1

# Game Loop
while playing:
    # Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Draw the current Game Board
    draw_board(spots)

    # If an invalid turn occurred, let the player know
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
            # Valid move
            spots[spot] = check_turn(turn)
            turn += 1
        # else: invalid move, same turn continues
    else:
        # Invalid input, same turn continues
        continue

    # Check if the game has ended
    if check_for_win(spots):
        playing, complete = False, True
    elif turn >= 9:
        playing = False

# Final screen update
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

# Final result
if complete:
    winner = 'Player 1' if check_turn(turn - 1) == 'X' else 'Player 2'
    print(f"{winner} Wins!")