import os 
import time

def logo():
    print("""\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣶⡎⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢱⣶⣶⣶⣶⣶⣶⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠛⢣⣤⣤⣤⣤⣤⣤⣤⣤⡄⠀⠈⠛⠛⠛⠛⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⠛⠛⠛⢣⣤⡄⠀⠀⠀⠀⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡸⠿⢇⣀⣀⠀⠀⠻⠿⢃⣀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠿⠿⢇⣀⡸⠿⠿⣀⣀⠀⠀⢸⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⢸⣿⡇⠀⠀⣿⣿⠀⠀⢸⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿⡇⠀⠀⠀⠀⣿⣿⠀⠀⢸⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⢸⣿⡇
⠀⠀⠀⠀⠀⠀⠀⢰⣶⡎⠉⠱⣶⣶⠉⠉⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⢸⣿⡇
⠀⠀⠀⠀⠀⣶⣶⡌⠉⢱⣶⡆⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⣴⣶⡎⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)

def closing_logo():
    print("""\
    ⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀
    ⠀⣤⡄⠀⢀⠎⠉⠉⠀⠀⠀⠈⠙⠻⣿⣿⣆⠀
    ⣸⣿⣷⠀⣼⡉⢉⣵⠀⢠⠂⠉⣢⠀⢹⣿⣿⡀
    ⣿⣿⣿⢠⠙⢍⣙⡿⠄⢜⣟⠙⡿⠁⢸⣿⣿⡇
    ⠘⣿⣿⣿⡀⠀⠉⣽⡻⠇⠀⠀⠀⠀⣸⣿⣿⡇
    ⠀⠈⠙⠻⡇⠀⠈⠀⠀⠀⠀⠀⠀⠀⡿⣿⡿⡇
    ⠀⠀⠀⠀⠹⠀⠀⠀⠀⠀⠀⣤⣶⣶⣾⣿⡇⡇
    ⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠙⠿⠿⠿⢟⣵⣷
    ⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⠀
    """)

def closing_tag():
    os.system("clear")
    print("Program Terminated")
    closing_logo()
    print("Have a good day!")
    time.sleep(1)
    os.system("clear")
    quit()

def main_menu_options():
        print("Main Menu")
        print("")
        print("1) Player menu")
        print("2) World menu")
        print("3) Server menu")
        print("4) Quit")
        print("")

def sub_menu_options(category):
    print(f"{category.title()} Menu")
    print("")
    print(f"1) Display all {category}s")
    print(f"2) Lookup {category} by Name")
    print(f"3) Add a {category}")
    print("4) Back to Main Menu")
    print("")

def loading():
    os.system("clear")
    print("loading...")
    time.sleep(1)
    os.system("clear")

def no_matches_found():
    print("Results: ")
    print("------------------")
    print("No matches found")
    print("------------------")
    time.sleep(2)
    os.system("clear")

def invalid_input():
    os.system("clear")
    print("Error!!! Invalid input, please try again!")
    time.sleep(1)
    os.system("clear")

def print_players(data):
    print(f"Username: {data.user_name} | " +\
    f"Role: {data.role} | " +\
    f"Experience: {data.exp} | " +\
    f"Skin: {data.skin} | " +\
    f"ID: {data.id} |")

def print_worlds(data):
    print(f"Name: {data.name} | " +\
    f"Seed: {data.seed} | " +\
    f"Spawn: {data.spawn} | " +\
    f"Players: {data.player_count} | " +\
    f"ID: {data.id} |")

def print_servers(data):
        print(f"Name: {data.server_name} | " +\
        f"IP address: {data.server_ip} |")

def disclaimer_for_add_to_server():
    print("***DISCLAIMER***\n"
        "If adding a new player or world to an existing server,\n"
        "please enter the existing server name and ip address in\n"
        "their respected fields.\n"
        "*******************\n")
