from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Player, Server, World
from sqlalchemy import desc

from helpers import (
    loading, no_matches_found, invalid_input,
    print_players, print_worlds, print_servers,
    disclaimer_for_add_to_server)

import os
import time

engine = create_engine("sqlite:///db/minecraft_model.db")
Session = sessionmaker(bind=engine)
session = Session()

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
        while True:
            print("Results: ")
            print("------------------")
            print_players(player_lookup_list)
            print("------------------")
            player_relations = input("Would you like to see related worlds or servers? " + \
                "(0=no 1=worlds 2=servers)...")
            if player_relations == "0":
                loading()
                break
            elif player_relations == "1":
                loading()
                if len(player_lookup_list.worlds) == 0:
                    no_matches_found()
                    break
                else:
                    print("Results: ")
                    print("------------------")
                    for world in player_lookup_list.worlds:
                        print_worlds(world)
                    print("------------------")
                    input("Press any key to continue...")
                    loading()
                    break
            elif player_relations == "2":
                loading()
                if len(player_lookup_list.servers)== 0:
                    no_matches_found()
                    break
                else:   
                    print("Results: ")
                    print("------------------")
                    for server in player_lookup_list.servers:
                        print_servers(server)
                    print("------------------")
                    input("Press any key to continue...")
                    loading()
                    break
            else:
                invalid_input()

def search_for_worlds(data_list, search_name):
    world_lookup_list = session.query(data_list).filter(data_list.name==search_name).first()
    if world_lookup_list == None:
        no_matches_found()
    else:
        while True:
            print("Results: ")
            print("------------------")
            print_worlds(world_lookup_list)
            print("------------------")
            world_relations = input("Would you like to see related players or servers? " + \
                "(0=no 1=players 2=servers)...")
            if world_relations == "0":
                loading()
                break
            elif world_relations == "1":
                loading()
                if len(world_lookup_list.players) == 0:
                    no_matches_found()
                    break
                else:
                    print("Results: ")
                    print("------------------")
                    for player in world_lookup_list.players:
                        print_players(player)
                    print("------------------")
                    input("Press any key to continue...")
                    loading()
                    break
            elif world_relations == "2":
                loading()
                if len(world_lookup_list.servers) == 0:
                    no_matches_found()
                    break
                else:
                    
                    print("Results: ")
                    print("------------------")
                    for server in world_lookup_list.servers:
                        print_servers(server)
                    print("------------------")
                    input("Press any key to continue...")
                    loading()
                    break
            else:
                invalid_input()

def search_for_servers(data_list, search_name):
    server_lookup_list = session.query(data_list).filter(data_list.server_name==search_name).first()
    if server_lookup_list == None:
        no_matches_found()
    else:
        while True:
            print("Results: ")
            print("------------------")  
            print_servers(server_lookup_list)
            print("------------------")
            server_relations = input("Would you like to see related players or worlds?" + \
                "(0=no 1=players 2=worlds)...")
            if server_relations == "0":
                loading()
                break
            elif server_relations == "1":
                loading()
                player_id_server_list = []

                for item in session.query(data_list).filter(data_list.server_name==search_name).all():
                    player_id_server_list.append(item.player_id)
                for id in player_id_server_list:
                    check = session.query(Player).filter(Player.id==id).all()
                    if len(check) == 0:
                        no_matches_found()
                        break
                    else:
                        print("Results: ")
                        print("------------------") 
                        for player_id in player_id_server_list:
                            player = session.query(Player).filter(Player.id==player_id).first()
                            print_players(player)
                        print("------------------")
                        input("Press any key to continue...")
                        loading()
                        break
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
                        break
                    else:
                        print("Results: ")
                        print("------------------") 
                        for world_id in world_id_server_list:
                            world = session.query(World).filter(World.id==world_id).first()
                            print_worlds(world)
                        print("------------------")
                        input("Press any key to continue...")
                        loading()
                        break
                break
            else:
                invalid_input()

def add_to_player():
    os.system("clear")
    while True:
        new_user_name = input("Please enter name (cannot be blank): ")
        if len(new_user_name) == 0:
            invalid_input()
            continue
        os.system("clear")
        break
    while True:
        new_role = input("Please enter role (Admin or Player): ")
        if new_role.lower() != "admin" and new_role.lower() != "player":
            invalid_input()
            continue
        os.system("clear")
        break
    while True:
        new_exp = input("Please enter experience level (must be integer): ")
        if new_exp.isdigit() == False:
            invalid_input()
            continue
        os.system("clear")
        break
    while True:
        new_skin = input("Please enter skin (cannot be blank): ")
        if len(new_skin) == 0:
            invalid_input()
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
    loading()

def add_to_world():
    os.system("clear")
    while True:
        new_name = input("Please enter name (cannot be blank): ")
        if len(new_name) == 0:
            invalid_input()
            continue
        os.system("clear")
        break
    while True:
        new_seed = input("Please enter seed (must be 6 digits): ")
        try:
            int(new_seed)
        except ValueError:
            invalid_input()
            continue
        if len(new_seed) != 6:
            invalid_input()
            continue
        os.system("clear")
        break  
    while True:          
        new_spawn = input("Please enter spawn point (must be an integer, can be negative): ")
        try:
            int(new_spawn)
        except ValueError:
            invalid_input()
            continue
        os.system("clear")
        break 
    while True: 
        new_player_count = input("Please enter player count (must be an integer greater than 0): ")
        if new_player_count.isdigit() == False:
            invalid_input()
            continue
        if new_player_count == "0":
            invalid_input()
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
    loading()

def add_to_server():
    os.system("clear")
    disclaimer_for_add_to_server()
    input("press any key to continue:")
    os.system("clear")
    while True:
        new_server_name = input("Please enter server name (cannot be blank): ")
        if len(new_server_name) == 0:
            invalid_input()
            continue
        os.system("clear")
        break
    while True:           
        new_server_ip = input("Please enter server ip (must be 5 digits): ")
        if new_server_ip.isdigit() == False or len(new_server_ip) != 5:
            invalid_input()
            continue
        os.system("clear")
        break 
    while True:
        new_player_id = input("Please enter player id (must be an integer greater than 0): ")
        if new_player_id.isdigit() == False or new_player_id == "0":
            invalid_input()
            continue
        os.system("clear")
        break
    while True:
        new_world_id = input("Please enter world id (must be an integer greater than 0): ")
        if new_world_id.isdigit() == False or new_world_id == "0":
            invalid_input()
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
        f"Player ID: {print_new_server.player_id} | " +\
        f"World ID: {print_new_server.world_id} |")
    print("------------------")
    input("Press any key to continue...")
    loading()