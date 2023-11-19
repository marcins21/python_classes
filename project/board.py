from settings import BOARD_HEIGH, BOARD_WIDTH


class Board:
    def __init__(self, board_name: str):
        self.width = BOARD_WIDTH
        self.heigh = BOARD_HEIGH
        self.board_name = board_name
        self.board = []
        self.spaces_between_other_board = 10

    def generate_board(self):
        for row in range(self.heigh):
            self.board.append([])
            for col in range(self.width):
                self.board[row].append("#")

    def show_game_board(self, other_board: "Board"):
        spaces_between_titles = (
            2 * (self.width) - len(self.board_name) + self.spaces_between_other_board
        )
        board_title = (
            f"\n{self.board_name}"  # By Default - Player Board Title
            + (" " * (spaces_between_titles)) # Spaces between name of boards
            + f"{other_board.board_name}"  # By Default - Bot Board Title
        )

        print(board_title)
        for row in range(self.heigh):
            for col in range(self.width):
                print(self.board[row][col], end=" ")
            print(end=(" " * self.spaces_between_other_board))
            for col2 in range(self.width):
                print(other_board.board[row][col2], end=" ")
            print()



