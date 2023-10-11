from prettytable import PrettyTable
from WinnerDeterminer import WinnerDeterminer

class MoveTable:
    def __init__(self, moves):
        self.moves = moves
        self.winner_determiner = WinnerDeterminer(moves).determine_winner

    def display_table(self):
        table = PrettyTable(["v PC\\User >"] + list(self.moves.values()))
        for player_move in self.moves:
            row = [self.moves[player_move]]
            row += [self.winner_determiner(player_move, computer_move) for computer_move in self.moves]
            table.add_row(row, divider=True)
        print(table)
