                                         # TASK 2 - TIC-TAC-TOE AI
                                                
                                                # Project

import math

# Display Board

def print_board(board):
    print()
    print("     |     |")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("     |     |")
    print()


# Check Winner

def check_winner(board):

    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:

        if board[a] == board[b] == board[c]:

            if board[a] == "X":
                return "X"

            elif board[a] == "O":
                return "O"

    return None


# Check Draw

def is_draw(board):

    for position in board:

        if position not in ["X", "O"]:
            return False

    return True


# Get Available Moves

def get_available_moves(board):

    moves = []

    for i in range(9):

        if board[i] not in ["X", "O"]:
            moves.append(i)

    return moves

# Minimax Algorithm

def minimax(board, depth, is_maximizing):

    winner = check_winner(board)

    # AI wins
    if winner == "O":
        return 10 - depth

    # Human wins
    elif winner == "X":
        return depth - 10

    # Draw
    elif is_draw(board):
        return 0

    # AI's turn
    if is_maximizing:

        best_score = -math.inf

        for move in get_available_moves(board):

            board[move] = "O"

            score = minimax(
                board,
                depth + 1,
                False
            )

            board[move] = str(move + 1)

            best_score = max(
                best_score,
                score
            )

        return best_score

    # Human's turn
    else:

        best_score = math.inf

        for move in get_available_moves(board):

            board[move] = "X"

            score = minimax(
                board,
                depth + 1,
                True
            )

            board[move] = str(move + 1)

            best_score = min(
                best_score,
                score
            )

        return best_score

# AI Best Move

def find_best_move(board):

    best_score = -math.inf
    best_move = None

    for move in get_available_moves(board):

        board[move] = "O"

        score = minimax(
            board,
            0,
            False
        )

        board[move] = str(move + 1)

        if score > best_score:

            best_score = score
            best_move = move

    return best_move


# Human Move

def human_move(board):

    while True:

        try:

            move = int(
                input("Enter your position (1-9): ")
            )

            if move < 1 or move > 9:

                print("Please enter a number between 1 and 9.")
                continue

            index = move - 1

            if board[index] in ["X", "O"]:

                print("That position is already occupied.")
                continue

            board[index] = "X"
            break

        except ValueError:

            print("Please enter a valid number.")


# Main Game

def play_game():

    board = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"
    ]

    print("\n===================================")
    print("       TIC-TAC-TOE AI")
    print("===================================")

    print("\nYou are X.")
    print("AI is O.")

    print("\nBoard positions:")
    print_board(board)

    while True:

        # Human turn
        print("Your turn.")

        human_move(board)

        print_board(board)

        winner = check_winner(board)

        if winner == "X":

            print("🎉 Congratulations! You won!")
            break

        if is_draw(board):

            print("It's a draw!")
            break

        # AI turn
        print("AI is thinking...")

        ai_move = find_best_move(board)

        board[ai_move] = "O"

        print_board(board)

        winner = check_winner(board)

        if winner == "O":

            print("🤖 AI wins! Better luck next time.")
            break

        if is_draw(board):

            print("It's a draw!")
            break


# Start Game

if __name__ == "__main__":
    play_game()