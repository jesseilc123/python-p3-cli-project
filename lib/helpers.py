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
    print("Results: ")
    print("------------------")
    print("No matches found")
    print("------------------")
    time.sleep(2)
    os.system("clear")

def invalid_input():
    os.system("clear")
    print("Invalid input, please try again!")
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

def display_all(category, data_list):
    os.system("clear")
    print("Getting results: ")
    print("------------------")
    time.sleep(1)
    if category == "player":
        for data in session.query(data_list).all():
            print_players(data)
        print("------------------")
    elif category == "world":
        for data in session.query(data_list).all():
            print_worlds(data)
        print("------------------")
    elif category == "server":
        new_serverlist = []
        for data in session.query(data_list).all():
            if data.server_name not in new_serverlist:
                new_serverlist.append(data.server_name)
        for item in new_serverlist:
            items_to_print = session.query(data_list).filter(data_list.server_name==item).first()
            print_servers(items_to_print)
        print("------------------")
        

def search_for_players(data_list, search_name):
    player_lookup_list = session.query(data_list).filter(data_list.user_name==search_name).first()
    if player_lookup_list == None:
        no_matches_found()
    else:
        print("Results: ")
        print("------------------")
        print_players(player_lookup_list)
        print("------------------")
        player_relations = input("Would you like to see related worlds or servers? " + \
            "(0=no 1=worlds 2=servers)...")
        if player_relations == "0":
            os.system("clear")
        elif player_relations == "1":
            loading()
            if len(player_lookup_list.worlds) == 0:
                no_matches_found()
            else:
                print("Results: ")
                print("------------------")
                for world in player_lookup_list.worlds:
                    print_worlds(world)
                print("------------------")
                input("Press any key to continue...")
                loading()
        elif player_relations == "2":
            loading()
            if len(player_lookup_list.servers)== 0:
                no_matches_found()
            else:   
                print("Results: ")
                print("------------------")
                for server in player_lookup_list.servers:
                    print_servers(server)
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
        print_worlds(world_lookup_list)
        print("------------------")
        world_relations = input("Would you like to see related players or servers? " + \
            "(0=no 1=players 2=servers)...")
        if world_relations == "0":
            os.system("clear")
        elif world_relations == "1":
            loading()
            if len(world_lookup_list.players) == 0:
                no_matches_found()
            else:
                print("Results: ")
                print("------------------")
                for player in world_lookup_list.players:
                    print_players(player)
                print("------------------")
                input("Press any key to continue...")
                os.system("clear")
        elif world_relations == "2":
            loading()
            if len(world_lookup_list.servers) == 0:
                no_matches_found()
            else:
                
                print("Results: ")
                print("------------------")
                for server in world_lookup_list.servers:
                    print_servers(server)
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
        print_servers(server_lookup_list)
        print("------------------")
        server_relations = input("Would you like to see related players or worlds?" + \
            "(0=no 1=players 2=worlds)...")
        if server_relations == "0":
            os.system("clear")
        elif server_relations == "1":
            loading()
            player_id_server_list = []

            for item in session.query(data_list).filter(data_list.server_name==search_name).all():
                player_id_server_list.append(item.player_id)
            for id in player_id_server_list:
                check = session.query(Player).filter(Player.id==id).all()
                if len(check) == 0:
                    no_matches_found()
                else:
                    print("Results: ")
                    print("------------------") 
                    for player_id in player_id_server_list:
                        player = session.query(Player).filter(Player.id==player_id).first()
                        print_players(player)
                    print("------------------")
                    input("Press any key to continue...")
                    os.system("clear")
                    break
        elif server_relations == "2":
            loading()
            world_id_server_list = []

            for item in session.query(data_list).filter(data_list.server_name==search_name).all():
                if item.world_id not in world_id_server_list:
                    world_id_server_list.append(item.world_id)
            for id in world_id_server_list:
                check = session.query(World).filter(World.id==id).all()
                if len(check) == 0:
                    no_matches_found()
                else:
                    print("Results: ")
                    print("------------------") 
                    for world_id in world_id_server_list:
                        world = session.query(World).filter(World.id==world_id).first()
                        print_worlds(world)
                    print("------------------")
                    input("Press any key to continue...")
                    os.system("clear")
                    break
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
    print_players(print_new_player)
    print("------------------")
    input("Press any key to continue...")
    os.system("clear")

def add_to_world():
    os.system("clear")
    while True:
        new_name = input("Please enter name: ")
        if len(new_name) == 0:
            os.system("clear")
            print("Error!!! Please enter a name.")
            time.sleep(1)
            os.system("clear")
            continue
        os.system("clear")
        break
    while True:
        new_seed = input("Please enter seed: ")
        if new_seed.isdigit() == False:
            os.system("clear")
            print("Error!!! Please enter a valid seed.")
            time.sleep(1)
            os.system("clear")
            continue
        os.system("clear")
        break  
    while True:          
        new_spawn = input("Please enter spawn point: ")
        try:
            int(new_spawn)
        except ValueError:
            os.system("clear")
            print("Error!!! Please enter a valid spawn point.")
            time.sleep(1)
            os.system("clear")
            continue
        os.system("clear")
        break 
    while True: 
        new_player_count = input("Please enter player count: ")
        if new_player_count.isdigit() == False:
            os.system("clear")
            print("Error!!! Please enter a valid player count.")
            time.sleep(1)
            os.system("clear")
            continue
        os.system("clear")
        break 

    world = World(
        name=new_name,
        seed=new_seed,
        spawn=new_spawn,
        player_count=new_player_count
    )

    session.add(world)
    session.commit()

    print_new_world = session.query(World).order_by(desc(World.id)).first()
    loading()
    print("Here is your new world!")
    print("------------------")
    print_worlds(print_new_world)
    print("------------------")
    input("Press any key to continue...")
    os.system("clear")

def add_to_server():
    os.system("clear")
    print("***DISCLAIMER***\n"
        "If adding a new player or world to an existing server\n"
        "enter the existing server name and ip address in their\n"
        "respected fields.\n"
        "*******************\n")
    while True:
        new_server_name = input("Please enter server name: ")
        if len(new_server_name) == 0:
            os.system("clear")
            print("Error!!! Please enter a name.")
            time.sleep(1)
            os.system("clear")
            continue
        os.system("clear")
        break
    while True:           
        new_server_ip = input("Please enter server ip: ")
        if new_server_ip.isdigit() == False:
            os.system("clear")
            print("Error!!! Please enter a valid server ip.")
            time.sleep(1)
            os.system("clear")
            continue
        os.system("clear")
        break 
    while True:
        new_player_id = input("Please enter player id: ")
        if new_player_id.isdigit() == False or new_player_id == "0":
            os.system("clear")
            print("Error!!! Please enter a valid player id.")
            time.sleep(1)
            os.system("clear")
            continue
        os.system("clear")
        break
    while True:
        new_world_id = input("Please enter world id: ")
        if new_world_id.isdigit() == False or new_world_id == "0":
            os.system("clear")
            print("Error!!! Please enter a valid world id.")
            time.sleep(1)
            os.system("clear")
            continue
        os.system("clear")
        break
    server = Server(
        server_name=new_server_name,
        server_ip=new_server_ip,
        player_id=new_player_id,
        world_id=new_world_id
    )

    session.add(server)
    session.commit()
    
    print_new_server = session.query(Server).order_by(desc(Server.id)).first()
    loading()
    print("Here is your new Server!")
    print("------------------")
    print(f"Name: {print_new_server.server_name} | " +\
        f"IP address: {print_new_server.server_ip} | " +\
        f"ID: {print_new_server.id} | " +\
        f"Player ID: {print_new_server.player_id} | " +\
        f"World ID: {print_new_server.world_id} |")
    print("------------------")
    input("Press any key to continue...")
    os.system("clear")