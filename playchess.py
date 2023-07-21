import chess
import chess.engine
import os

def play_game():
    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

    # Choose color
    color = input("Choose your color (w/b): ")
    while color not in ["w", "b"]:
        color = input("Invalid input. Choose your color (w/b): ")
    human_is_white = color == "w"

    # Choose difficulty
    difficulty = input("Choose difficulty level (0-20): ")
    while not difficulty.isdigit() or int(difficulty) < 0 or int(difficulty) > 20:
        difficulty = input("Invalid input. Choose difficulty level (0-20): ")
    engine.configure({"Skill Level": int(difficulty)})

    while not board.is_game_over():
        os.system('clear')
        display_board(board, human_is_white)
        if board.turn == human_is_white:
            move = input("Enter your move (from-to, e4e5) : ")
            try:
                board.push_san(move)
            except ValueError:
                print("Invalid move")
        else:
            result = engine.play(board, chess.engine.Limit(time=2.0))
            board.push(result.move)

    engine.quit()
    print(board.result())

def display_board(board, human_is_white):
    board_str = board.unicode(invert_color=not human_is_white, borders=True).replace(".", " ")
    board_str = board_str.replace("|", " | ")
    board_str = "\n".join([" ".join(line) if line[0] == " " else line for line in board_str.split("\n")])
    board_str = board_str.replace(" - - - - - - - - - - - - - - - - -", "- - - - - - - - - - - - - - - - -")
    board_str = board_str.replace("  a   b   c   d   e   f   g   h", " a   b   c   d   e   f   g   h")
    board_str = board_str.replace("⭘", " ")
    print(board_str)

if __name__ == "__main__":
    play_game()
