from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Player, Server, World

def main_menu():
    choice = 0

    print("***Enter the corresponding number***")
    print("1) Player menu")
    print("2) World menu")
    print("3) Server menu")
    print("4) Exit")

    while choice !=4:
        choice = int(input())
        if choice == 1:
            sub_menu("Player")
        if choice == 2:
            sub_menu("World")
        if choice == 3:
            sub_menu("Server")
        if choice == 4:
            print("Quiting Program")
    print("Program Terminated")

def sub_menu(category):
    sub_choice = 0
    while sub_choice != 3:
        print(f"***{category} Menu***")
        print(f"1) Lookup {category}")
        print(f"2) Display all {category}s")
        print("3) Back to Main Menu")
        sub_choice = int(input())

        if sub_choice == 1:
            print("test for look up")
            item = session.query()
        if sub_choice == 2:
            print("test for display")
        if sub_choice == 3:
            print("test for back")
    main_menu()

    
