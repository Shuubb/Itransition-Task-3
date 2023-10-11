class WinnerDeterminer:
    def __init__(self, moves):
        self.moves = moves

    def determine_winner(self, player_move, computer_move):
        moves_len = len(self.moves)
        diff = (int(computer_move) - int(player_move)) % moves_len

        if diff == 0:
            return "\033[1;33mIt's a Tie!\033[0m"
        elif diff <= moves_len // 2:
            return "\033[1;32mYou Win!\033[0m"
        else:
            return "\033[1;31mYou Lose!\033[0m"
