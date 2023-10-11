from MoveValidator import MoveValidator
import sys
from Game import Game

if __name__ == "__main__":
    args = sys.argv[1:]
    if MoveValidator.validate(args):
        moves = {str(index + 1): move for index, move in enumerate(args)}
        game = Game(moves)
        game.start_game()