import os
import settings
from termcolor import colored

from board import Board


def game_menu():
    print("\n1) Hit Cell\n2) Randomize Ships \n3) Exit")


def starting_menu_options():
    print("\n1) Set Username\n2) Start New Game\n3) Exit")


def game(player_board: "Board", bot_board: "Board", info=""):
    os.system("cls||clear")
    print(info)

    while True:
        game_menu()
        player_board.show_game_board(bot_board)

        try:
            user_options_menu_input = int(input(colored("Option: ", "light_blue")))
        except ValueError:
            os.system("cls||clear")
            print(
                colored(
                    "\nYou didn't provide digit as a starting option\n",
                    "red",
                )
            )
            continue

        if (user_options_menu_input < 1) or (user_options_menu_input > 3):
            os.system("cls||clear")
            print(
                colored(
                    "\nYou didn't provide any of above options \n",
                    "red",
                )
            )
            continue

        # Hit logic
        if user_options_menu_input == 1:
            os.system("cls||clear")
            pass

        # Randomize ships placement on the board logic
        if user_options_menu_input == 2:
            os.system("cls||clear")
            player_board.board[0][0] = "X"
            pass

        # Exit
        if user_options_menu_input == 3:
            starting_menu(colored("\nExiting into starting menu\n", "red"))
            break


def starting_menu(error=""):
    os.system("cls||clear")
    print(error)

    while True:
        starting_menu_options()

        try:
            user_options_menu_input = int(input(colored("Option: ", "light_blue")))
        except ValueError:
            os.system("cls||clear")
            print(
                colored(
                    "\nYou didn't provide digit as a starting option\n",
                    "red",
                )
            )
            continue

        if (user_options_menu_input < 1) or (user_options_menu_input > 3):
            os.system("cls||clear")
            print(
                colored(
                    "\nYou didn't provide any option listed above in starting menu ... \n",
                    "red",
                )
            )
            continue

        if user_options_menu_input == 1:
            user_name = input(colored("Set Username: ", "light_blue"))
            settings.USER_NAME = user_name
            os.system("cls||clear")
            print(colored("\nUsername Set Succesfully", "green"))

        # Starting game
        if user_options_menu_input == 2:
            player_board = Board(settings.USER_NAME)
            bot_board = Board(settings.BOT_NAME)
            try:
                player_board.generate_board()
                bot_board.generate_board()
            except Exception:
                print(
                    colored("\nUnexpected Error Occcured while creating boards", "red")
                )
                return

            # Game
            game(
                player_board=player_board,
                bot_board=bot_board,
                info=colored("\nBoard Created Successfully", "green"),
            )

        # User Exiting app
        if user_options_menu_input == 3:
            print("\nExiting!\n")
            exit(0)


starting_menu()
