from settings import (
    BOARD_HEIGH,
    BOARD_WIDTH,
    AMOUNT_OF_SMALL_SHIPS,
    AMOUNT_OF_MEDIUM_SHIPS,
    AMOUNT_OF_LARGE_SHIPS,
)
import ship
import random
from termcolor import colored


class Board:
    def __init__(self, board_name: str):
        self.width = BOARD_WIDTH
        self.heigh = BOARD_HEIGH
        self.board_name = board_name
        self.board = []
        self.spaces_between_other_board = 10
        self.ships = []

    def generate_board(self):
        for row in range(self.heigh):
            self.board.append([])
            for col in range(self.width):
                self.board[row].append("#")

    def add_ship(self, ship: "ship.Ship"):
        self.ships.append(ship)

    def place_ship(self, ship: "ship.Ship"):
        for coord in ship.cords:
            row, col = coord
            self.board[row][col] = colored("X", "green")

    def is_valid_position(self, ship: "ship.Ship"):
        for coord in ship.cords:
            row, col = coord
            if (
                row < 0
                or row >= self.heigh
                or col < 0
                or col >= self.width
                or self.board[row][col] == "X"
            ):
                return False
        return True

    def randomize_ships_across_board(self):
        # Small ships
        for _ in range(AMOUNT_OF_SMALL_SHIPS):
            small_ship = ship.SmallShip([])
            self.randomly_place_ship(small_ship)

        # Medium ships
        for _ in range(AMOUNT_OF_MEDIUM_SHIPS):
            medium_ship = ship.MediumShip([])
            self.randomly_place_ship(medium_ship)

        # Large ships
        for _ in range(AMOUNT_OF_LARGE_SHIPS):
            large_ship = ship.LargeShip([])
            self.randomly_place_ship(large_ship)

    def randomly_place_ship(self, ship: "ship.Ship"):
        while True:
            orientation = random.choice(["horizontal", "vertical"])
            start_row = random.randint(0, self.heigh - 1)
            start_col = random.randint(0, self.width - 1)
            ship.cords = self.calculate_ship_coordinates(
                start_row, start_col, ship.width, orientation
            )

            if self.is_valid_position(ship):
                self.place_ship(ship)
                self.add_ship(ship)
                break

    def calculate_ship_coordinates(self, start_row, start_col, ship_width, orientation):
        if orientation == "horizontal":
            return [(start_row, start_col + i) for i in range(ship_width)]
        else:  # vertical
            return [(start_row + i, start_col) for i in range(ship_width)]


def show_game_board(player_board: "Board", bot_board: "Board"):
    spaces_between_titles = (
        2 * (player_board.width)
        - len(player_board.board_name)
        + player_board.spaces_between_other_board
    )
    board_title = (
        f"\n{player_board.board_name}"  # By Default - Player Board Title
        + (" " * (spaces_between_titles))  # Spaces between name of boards
        + f"{bot_board.board_name}"  # By Default - Bot Board Title
    )

    print(board_title)
    for row in range(player_board.heigh):
        for col in range(player_board.width):
            print(player_board.board[row][col], end=" ")
        print(end=(" " * player_board.spaces_between_other_board))
        for col2 in range(player_board.width):
            print(bot_board.board[row][col2], end=" ")
        print()
