from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Player, Server, World

engine = create_engine("sqlite:///db/minecraft_model.db")
Session = sessionmaker(bind=engine)
session = Session()

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
            sub_menu("player", Player)
        if choice == 2:
            sub_menu("world", World)
        if choice == 3:
            sub_menu("server", Server)
        if choice == 4:
            print("Quiting Program...")
    print("Program Terminated")
    quit()

def sub_menu(category, data_list):
    sub_choice = 0
    while sub_choice != 3:
        print(f"***{category.title()} Menu***")
        print(f"2) Display all {category}s")
        print(f"1) Lookup {category} by Name")
        print("3) Back to Main Menu")
        sub_choice = int(input())

        if sub_choice == 1:
            for data in session.query(data_list).all():
                print(data)
        if sub_choice == 2:
            search_name = input("Please type the name...")
            if category == "player":
                print(session.query(data_list).filter(data_list.user_name==search_name).first())
            elif category == "world":
                print(session.query(data_list).filter(data_list.name==search_name).first())
            elif category == "server":
                print(session.query(data_list).filter(data_list.server_name==search_name).first())
        if sub_choice == 3:
            print("test for back")
    main_menu()

def add_to_player():
    pass

def add_to_world():
    pass

def add_to_server():
    pass