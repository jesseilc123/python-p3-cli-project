from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Player, Server, World
from sqlalchemy import desc

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
    while sub_choice != 4:
        print(f"***{category.title()} Menu***")
        print(f"1) Display all {category}s")
        print(f"2) Lookup {category} by Name")
        print(f"3) Add a {category}")
        print("4) Back to Main Menu")
        sub_choice = int(input())

        if sub_choice == 1:
            for data in session.query(data_list).all():
                print(data)
        if sub_choice == 2:
            search_name = input("Please type the name: ")
            if category == "player":
                player_lookup_list = session.query(data_list).filter(data_list.user_name==search_name).first()
                if len(player_lookup_list) < 0:
                    print("No matches found")
                else:
                    print(player_lookup_list)
            elif category == "world":
                world_lookup_list = session.query(data_list).filter(data_list.name==search_name).first()
                if len(world_lookup_list) < 0:
                    print("No matches found")
                else:
                    print(world_lookup_list)
            elif category == "server":
                server_lookup_list = session.query(data_list).filter(data_list.server_name==search_name).all()
                for server in server_lookup_list:
                    print(server)
        if sub_choice == 3:
            if category == "player":
                add_to_player()
            elif category == "world":
                add_to_world()
            elif category == "server":
                add_to_server()
        if sub_choice == 4:
            print("test for back")
    main_menu()

def add_to_player():
    new_user_name = input("Please enter name: ")
    new_role = input("Please enter role: ")
    new_exp = input("Please enter experience level: ")
    new_skin = input("Please enter skin: ")

    player = Player(
        user_name=new_user_name,
        role=new_role,
        exp=new_exp,
        skin=new_skin
    )

    session.add(player)
    session.commit()

    print(session.query(Player).order_by(desc(Player.id)).first())

def add_to_world():
    new_name = input("Please enter name: ")
    new_seed = input("Please enter seed: ")
    new_spawn = input("Please enter spawn point: ")
    new_player_count = input("Please enter player count: ")
    world = World(
        name=new_name,
        seed=new_seed,
        spawn=new_spawn,
        player_count=new_player_count
    )

    session.add(world)
    session.commit()

    print(session.query(World).order_by(desc(World.id)).first())

def add_to_server():
    new_server_name = input("Please enter server name: ")
    new_server_ip = input("Please enter server ip: ")
    new_player_id = input("Please enter player id: ")
    new_world_id = input("Please enter world id: ")
    server = Server(
        server_name=new_server_name,
        server_ip=new_server_ip,
        player_id=new_player_id,
        world_id=new_world_id
    )

    session.add(server)
    session.commit()

    print(session.query(Server).order_by(desc(Server.id)).first())