import random
from MoveTable import MoveTable
from helperFunctions import printErr
from HMACGenerator import HMACGenerator
from WinnerDeterminer import WinnerDeterminer

class Game:
    # Initialize the game with available moves, helpers, 
    # an HMAC generator, and a winner determiner.
    def __init__(self, moves) -> None:
        self.moves = moves
        self.helpers = {'0': "exit", '?': 'help'}
        self.hmac_generator = HMACGenerator()
        self.winner_determiner = WinnerDeterminer(moves)

    # Print the available moves and helper options.
    def print_available_moves(self) -> None:
        print('\033[93m' + 'Available moves:')
        for key, move in self.moves.items():
            print(f"{key} - {move}")
        for key, helper in self.helpers.items():
            print(f"{key} - {helper}")
        print('\033[0m')

    # Start the game by determining the computer's move, 
    # printing available moves, and handling the player's move.
    def start_game(self) -> None:
        
        print("\n")
        computer_move = self.computers_move()
        
        self.print_available_moves()

        player_move = self.players_move()

        print("\033[1;34m" + "Computer Move: "  + self.moves[computer_move] + "\033[0m")

        result = self.winner_determiner.determine_winner(player_move, computer_move)

        print(result + "\nHMAC Key: " + str(self.hmac_generator.key) + '\n')

        exit()

    # Get the player's move and respond to it.
    def players_move(self) -> str:
        move = input("\033[1m\033[4m" + "Enter your Move" + "\033[0m: ")
        self.respond_to_move(move)
        return move
    
    # Handle the player's move or provide help/exit options.
    def respond_to_move(self, move) -> None:
        if move == '0':
            print('Bye!')
        elif move == '?':
            move_table = MoveTable(self.moves)
            move_table.display_table()
        elif not move in self.moves:
            printErr("Incorrect Move!")
        else:
            print("\033[1;35m" + "Your move: "  + self.moves[move])
            return
        
        exit()

    # Generate a random move for the computer, 
    # compute HMAC, and return the move.
    def computers_move(self) -> str:
        random_move_key = random.choice(list(self.moves))
        random_move = self.moves[random_move_key]
        hmac = self.hmac_generator.compute_hmac(random_move)
        print("HMAC: " + str(hmac))
        return random_move_key