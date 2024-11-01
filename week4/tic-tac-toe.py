class TicTacToe:
    def __init__(self):
        # Initialise the game board with empty spaces
        self.__board = [" " for _ in range(9)]

    def __display_board(self):
        """Display the current state of the board."""
        # TODO: Display the board as a 3 by 3 grid

    def __player_move(self):
        """Handle the player's move."""
        position = int(input("Enter your move (0-8): "))
        # TODO: While the position is invalid, ask the user to enter it again.
        self.__board[position] = "X"

    def run(self):
        """Main game loop."""
        print("Welcome to Tic-Tac-Toe.\nYou are player X. I am player O.\n")
        while True:
            self.__display_board()
            self.__player_move()


# Example usage:
if __name__ == "__main__":
    # TODO: Instantiate and start the game
    pass
