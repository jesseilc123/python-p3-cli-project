from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Player, Server, World
from sqlalchemy import desc

import os
import time

engine = create_engine("sqlite:///db/minecraft_model.db")
Session = sessionmaker(bind=engine)
session = Session()

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
    
def closing():
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
        print("4) Exit")
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
    print("No matches found")
    time.sleep(1)
    os.system("clear")

def invalid_input():
    os.system("clear")
    print("Invalid input, please try again!")
    time.sleep(1)
    os.system("clear")

def display_all(category, data_list):
    os.system("clear")
    print("Getting results: ")
    print("------------------")
    time.sleep(1)
    if category == "player":
        for data in session.query(data_list).all():
            print(f"Username: {data.user_name} | " +\
                  f"Role: {data.role} | " +\
                  f"Experience: {data.exp} | " +\
                  f"Skin: {data.skin}")
        print("------------------")
    elif category == "world":
        for data in session.query(data_list).all():
            print(f"Name: {data.name} | " +\
                  f"Seed: {data.seed} | " +\
                  f"Spawn: {data.spawn} | " +\
                  f"Players: {data.player_count}")
        print("------------------")
    elif category == "server":
        new_serverlist = []
        for data in session.query(data_list).all():
            if data.server_name not in new_serverlist:
                new_serverlist.append(data.server_name)
        for item in new_serverlist:
            items_to_print = session.query(data_list).filter(data_list.server_name==item).first()
            print(f"Name: {items_to_print.server_name} | " +\
                  f"IP address: {items_to_print.server_ip}")
        print("------------------")
        

def search_for_players(data_list, search_name):
    player_lookup_list = session.query(data_list).filter(data_list.user_name==search_name).first()
    if player_lookup_list == None:
        no_matches_found()
    else:
        print("Results: ")
        print("------------------")
        print(f"Username: {player_lookup_list.user_name} | " +\
                f"Role: {player_lookup_list.role} | " +\
                f"Experience: {player_lookup_list.exp} | " +\
                f"Skin: {player_lookup_list.skin}")
        print("------------------")
        player_relations = input("Would you like to see related worlds or servers? " + \
            "(0=no 1=worlds 2=servers)...")
        if player_relations == "0":
            loading()
        elif player_relations == "1":
            loading()
            print("Results: ")
            print("------------------")
            for world in player_lookup_list.worlds:
                print(f"Name: {world.name} | " +\
                  f"Seed: {world.seed} | " +\
                  f"Spawn: {world.spawn} | " +\
                  f"Players: {world.player_count}")
            print("------------------")
            input("Press any key to continue...")
            loading()
        elif player_relations == "2":
            loading()
            print("Results: ")
            print("------------------")
            for server in player_lookup_list.servers:
                print(f"Server Name: {server.server_name} | " +\
                    f"Server IP: {server.server_ip} | ")
            print("------------------")
            input("Press any key to continue...")
            loading()
        else:
            invalid_input()

def search_for_worlds(data_list, search_name):
    world_lookup_list = session.query(data_list).filter(data_list.name==search_name).first()
    if world_lookup_list == None:
        no_matches_found()
    else:
        print("Results: ")
        print("------------------")
        print(f"Name: {world_lookup_list.name} | " +\
                f"Seed: {world_lookup_list.seed} | " +\
                f"Spawn: {world_lookup_list.spawn} | " +\
                f"Players: {world_lookup_list.player_count}")
        print("------------------")
        world_relations = input("Would you like to see related players or servers? " + \
            "(0=no 1=players 2=servers)...")
        if world_relations == "0":
            loading()
        elif world_relations == "1":
            loading()
            print("Results: ")
            print("------------------")
            for player in world_lookup_list.players:
                print(f"Username: {player.user_name} | " +\
                    f"Role: {player.role} | " +\
                    f"Experience: {player.exp} | " +\
                    f"Skin: {player.skin}")
            print("------------------")
            input("Press any key to continue...")
            os.system("clear")
        elif world_relations == "2":
            loading()
            print("Results: ")
            print("------------------")
            for server in world_lookup_list.servers:
                print(f"Server Name: {server.server_name} | " +\
                    f"Server IP: {server.server_ip} | ")
            print("------------------")
            input("Press any key to continue...")
            os.system("clear")
        else:
            invalid_input()

def search_for_servers(data_list, search_name):
    server_lookup_list = session.query(data_list).filter(data_list.server_name==search_name).first()
    if server_lookup_list == None:
        no_matches_found()
    else:
        print("Results: ")
        print("------------------")       
        print(f"Server Name: {server_lookup_list.server_name} | " +\
            f"Server IP: {server_lookup_list.server_ip} | ")
        print("------------------")
        server_relations = input("Would you like to see related players or worlds?" + \
            "(0=no 1=players 2=worlds)...")
        if server_relations == "0":
            loading()
        elif server_relations == "1":
            loading()
            player_id_server_list = []

            for item in session.query(data_list).filter(data_list.server_name==search_name).all():
                player_id_server_list.append(item.player_id)

            print("Results: ")
            print("------------------") 
            for player_id in player_id_server_list:
                player = session.query(Player).filter(Player.id==player_id).first()
                print(f"Username: {player.user_name} | " +\
                    f"Role: {player.role} | " +\
                    f"Experience: {player.exp} | " +\
                    f"Skin: {player.skin}")
            print("------------------")
            input("Press any key to continue...")
            os.system("clear")
        elif server_relations == "2":
            loading()
            world_id_server_list = []

            for item in session.query(data_list).filter(data_list.server_name==search_name).all():
                if item.world_id not in world_id_server_list:
                    world_id_server_list.append(item.world_id)
            
            print("Results: ")
            print("------------------") 
            for world_id in world_id_server_list:
                world = session.query(World).filter(World.id==world_id).first()
                print(f"Name: {world.name} | " +\
                        f"Seed: {world.seed} | " +\
                        f"Spawn: {world.spawn} | " +\
                        f"Players: {world.player_count}")
            print("------------------")
            input("Press any key to continue...")
            os.system("clear")
        else:
            invalid_input()

def add_to_player():
    os.system("clear")
    while True:
        new_user_name = input("Please enter name: ")
        if len(new_user_name) == 0:
            os.system("clear")
            print("Error!!! Please enter a name.")
            time.sleep(1)
            os.system("clear")
            continue
        os.system("clear")
        break
    while True:
        new_role = input("Please enter role (Admin or Player): ")
        if new_role.lower() != "admin" and new_role.lower() != "player":
            os.system("clear")
            print("Error!!! Please enter a valid Role (Admin or Player).")
            time.sleep(1)
            os.system("clear")
            continue
        os.system("clear")
        break
    while True:
        new_exp = input("Please enter experience level: ")
        if new_exp.isdigit() == False:
            os.system("clear")
            print("Error!!! Please enter a valid experience level.")
            time.sleep(1)
            os.system("clear")
            continue
        os.system("clear")
        break
    while True:
        new_skin = input("Please enter skin: ")
        if len(new_skin) == 0:
            os.system("clear")
            print("Error!!! Please enter a skin.")
            time.sleep(1)
            os.system("clear")
            continue
        os.system("clear")
        break

    player = Player(
        user_name=new_user_name,
        role=new_role.title(),
        exp=new_exp,
        skin=new_skin.title()
    )

    session.add(player)
    session.commit()

    print_new_player = session.query(Player).order_by(desc(Player.id)).first()
    loading()
    print("Here is your new player!")
    print("------------------")
    print(f"Username: {print_new_player.user_name} | " +\
    f"Role: {print_new_player.role} | " +\
    f"Experience: {print_new_player.exp} | " +\
    f"Skin: {print_new_player.skin}")
    print("------------------")
    input("Press any key to continue...")
    os.system("clear")

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
    new_server_ip = int(new_server_ip)
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