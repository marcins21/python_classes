from settings import (
    BOARD_HEIGH,
    BOARD_WIDTH,
    AMOUNT_OF_SMALL_SHIPS,
    AMOUNT_OF_MEDIUM_SHIPS,
    AMOUNT_OF_LARGE_SHIPS,
    SPACES_BETWEEN_OTHER_BOARD,
    USER_NAME,
    SPACE_BETWEEN_TITLES,
    BOT_NAME,
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


def show_game_board(
    player_board: "Board", bot_board: "Board", bot_title="", user_name=""
):
    BOARD_TITLE = (
        f"\n{user_name}"  # By Default - Player Board Title
        + (" " * (SPACE_BETWEEN_TITLES))  # Spaces between name of boards
        + f"{BOT_NAME}"  # By Default - Bot Board Title
    )

    print(BOARD_TITLE + bot_title)

    index_width = len(str(max(player_board.width, bot_board.width - 5)))

    print(" " * len(BOARD_TITLE), end="")
    print("")
    print(end=" ")
    for col in range(player_board.width):
        print(f" {col:>{index_width}}", end="")
    print(end=(" " * SPACES_BETWEEN_OTHER_BOARD))

    print(end=(" " * 3))
    for col2 in range(bot_board.width):
        print(f" {col2:>{index_width}}", end="")
    print()

    for row in range(player_board.heigh):
        print(f"{row:2} ", end="")

        # Print player board
        for col in range(player_board.width):
            print(player_board.board[row][col], end="  ")
        print(end=(" " * SPACES_BETWEEN_OTHER_BOARD))

        print(f"{row:2} ", end="")

        # Print bot board
        for col2 in range(bot_board.width):
            print(bot_board.board[row][col2], end="  ")
        print()

    # Previus Version, not including indecies

    # print(BOARD_TITLE + bot_title)
    # for row in range(player_board.heigh):
    #     for col in range(player_board.width):
    #         print(player_board.board[row][col], end=" ")
    #     print(end=(" " * SPACES_BETWEEN_OTHER_BOARD))
    #     for col2 in range(player_board.width):
    #         print(bot_board.board[row][col2], end=" ")
    #     print()
