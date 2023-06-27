from sub_menu_helpers import (
    display_all, search_for_players,
    search_for_worlds, search_for_servers, add_to_player,
    add_to_server, add_to_world)
from helpers import (
    logo, loading, invalid_input, main_menu_options,
    sub_menu_options, closing_tag)

from db.models import Player, World, Server

import os
import time

if __name__ == '__main__':
    os.system("clear")
    print("***Welcome to my Minecraft Database***")
    logo()
    input("Press any button to continue...")
    os.system("clear")
    
    def main_menu():
        os.system("clear")
        choice = 0

        main_menu_options()

        while choice != "4":
            choice = input("Enter the corresponding number: ")
            if choice == "1":
                loading()
                sub_menu("player", Player)
            if choice == "2":
                loading()
                sub_menu("world", World)
            if choice == "3":
                loading()
                sub_menu("server", Server)
            if choice == "4":
                os.system("clear")
                print("Quiting Program...")
                time.sleep(1)
            else:
                invalid_input()
                main_menu()
        closing_tag()

    def sub_menu(category, data_list):
        sub_choice = 0
        os.system("clear")

        while sub_choice != "4":
            sub_menu_options(category)
            sub_choice = input("Enter the corresponding number: ")
            if sub_choice == "1":
                display_all(category, data_list)
                cont = input("Continue? (Y=continue AnyKey=Main Menu)...")
                if cont.lower() != "y":
                    loading()
                    break
                loading()
            elif sub_choice == "2":
                os.system("clear")
                search_name = input("Please type the name: ")
                loading()
                if category == "player":
                    search_for_players(data_list, search_name)
                elif category == "world":
                    search_for_worlds(data_list, search_name)
                elif category == "server":
                    search_for_servers(data_list, search_name)
            elif sub_choice == "3":
                if category == "player":
                    add_to_player()
                elif category == "world":
                    add_to_world()
                elif category == "server":
                    add_to_server()
            elif sub_choice == "4":
                loading()
                break
            else:
                invalid_input()
        main_menu()

    main_menu()
