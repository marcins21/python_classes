from board import Board
from termcolor import colored
import settings
import os

def game_menu():
    print("\n1) Hit Cell\n2) New Game\n3) Exit")

def starting_menu_options():
    print("\n1) Set Username\n2) Start Game\n3) Exit")





def starting_menu():
    os.system('cls||clear')
    starting_menu_options()

    while True:
        try:
            user_options_menu_input = int(input(colored('Option: ','light_blue')))
        except ValueError:
            print(colored("\nYou didn't provide digit as a starting option, Exiting ....\n","red"))
            return

        if (user_options_menu_input < 1) or (user_options_menu_input > 3):
            print(colored("\nYou didn't provide any option listed above in starting menu, Exiting ... \n","red"))
            return


        if user_options_menu_input == 1:
            user_name = input(colored("Set Username: ","light_blue"))
            settings.USER_NAME = user_name
            os.system('cls||clear')
            print(colored("\nUsername Set Succesfully", "green"))
            starting_menu_options()

        # Starting game
        if user_options_menu_input == 2:


        # User Exiting app
        if user_options_menu_input == 3:
            print("\nExiting!\n")
            break


starting_menu()