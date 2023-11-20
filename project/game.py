import os
import random
import time
import settings
from termcolor import colored

from board import Board, show_game_board


def game_menu():
    print(
        "\n1) Hit Cell\n2) Randomize Ships \n3) Exit",
        "\n" + colored("4) Cheats", "dark_grey", attrs=["dark"]),
    )


def starting_menu_options():
    print("\n1) Set Username\n2) Start New Game\n3) Exit")


def validate_user_hit(x: str, y: str):
    try:
        x, y = int(x), int(y)
    except ValueError:
        print(colored("\nYou didn't provide integer coordinates try again", "red"))
        return None, None

    if 0 <= x < settings.BOARD_HEIGH and 0 <= y < settings.BOARD_WIDTH:
        return x, y

    print(
        colored(
            f"\nYou didn't provide right coordinates try again coords between {settings.BOARD_WIDTH}-{settings.BOARD_HEIGH}",
            "red",
        )
    )
    return None, None


def game(player_board: "Board", bot_board: "Board", info="", cst_name=""):
    os.system("cls||clear")
    print(info)

    while True:
        game_menu()
        show_game_board(
            player_board=player_board,
            bot_board=bot_board,
            bot_title=settings.BOT_THINK,
            user_name=cst_name,
        )

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

        if (user_options_menu_input < 1) or (user_options_menu_input > 4):
            os.system("cls||clear")
            print(
                colored(
                    "\nYou didn't provide any of above options \n",
                    "red",
                )
            )
            continue

        if user_options_menu_input == 1:
            user_hit_x, user_hit_y = input("Enter 'x' 'y': ").split()
            os.system("cls||clear")

            x, y = validate_user_hit(user_hit_x, user_hit_y)
            if (x and y) or x == 0 or y == 0:
                # Player Shoot
                bot_board.board[x][y] = colored("H", "red")

                player_hit = False
                player_win = False
                player_destroy=False
                for ship in bot_board.ships:
                    if ship.is_hit((x, y)):
                        player_hit = True
                        if ship.is_destroyed():
                            bot_board.ships.remove(ship)
                            player_destroy=True

                            # User win
                            if len(bot_board.ships) == 0:
                                player_win = True

                if player_hit:
                    os.system("cls||clear")
                    print("PLAYER: ", colored("HIT", "green"))

                if player_destroy:
                    os.system("cls||clear")
                    print("PLAYER: ", colored("DESTROYED!!!", "green"))

                if not player_hit:
                    os.system("cls||clear")
                    print("PLAYER: ", colored("MISS", "green"))

                if player_win:
                    os.system("cls||clear")
                    print(colored(f"{settings.USER_NAME} WIN!", "green"))
                    break

                # Bot Shoot
                bot_turn_x = random.randrange(0, settings.BOARD_HEIGH)
                bot_turn_y = random.randrange(0, settings.BOARD_WIDTH)
                time.sleep(0.1)

                player_board.board[bot_turn_x][bot_turn_y] = colored("H", "red")

                bot_hit = False
                bot_win = False
                bot_destroy=False
                for ship in player_board.ships:
                    if ship.is_hit((x, y)):
                        bot_hit = True
                        if ship.is_destroyed():
                            player_board.ships.remove(ship)
                            bot_destroy=True
                            # Bot win
                            if len(player_board.ships) == 0:
                                bot_win = True

                if bot_hit:
                    print(
                        "BOT: ",
                        colored(
                            f"BOT Got your ship at {bot_turn_x} - {bot_turn_y}",
                            "red",
                        ),
                    )
                if bot_destroy:
                    print(
                        "BOT: ",
                        colored(
                            f"BOT Got your WHOLE! ship at {bot_turn_x} - {bot_turn_y} DESTROYED!",
                            "red",
                        ),
                    )

                if not bot_hit:
                    print(
                        "BOT: ",
                        colored(
                            f"BOT Miss {bot_turn_x} - {bot_turn_y} Ufff... ", "red"
                        ),
                    )
                if bot_win:
                    os.system("cls||clear")
                    print(colored(f"{settings.BOT_NAME} WIN!", "red"))
                    break

        # Randomize ships placement on the board logic
        if user_options_menu_input == 2:
            os.system("cls||clear")
            player_board.randomize_ships_across_board()
            bot_board.randomize_ships_across_board()
            settings.BOT_THINK = colored(
                " Bot thinking about his next move".title(),
                "red",
                "on_black",
                ["bold", "blink"],
            )

        # Cheating option :)
        if user_options_menu_input == 4:
            os.system("cls||clear")
            print(colored("\nCHEATS ACTIVATED\nBOT SHIPS POSITIONS", "green"))
            for ship in bot_board.ships:
                print(
                    colored("BOT SHIP:", "dark_grey"),
                    f"{ship.__class__.__name__} Coordinates: {ship.cords}",
                )

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
                cst_name=settings.USER_NAME,
            )

        # User Exiting app
        if user_options_menu_input == 3:
            print("\nExiting!\n")
            exit(0)


starting_menu()
