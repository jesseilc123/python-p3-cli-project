from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Player, Server, World

from faker import Faker
import random

if __name__ == '__main__':
    engine = create_engine("sqlite:///minecraft_model.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Player).delete()
    session.query(Server).delete()
    session.query(World).delete()

    fake = Faker()

    players = []
    roles = ["admin", "player"]
    skins = ["Dog", "Fish", "Cat", "Axolotl", "Base Skin"]
    for i in range(30):
        player = Player(
            user_name=fake.unique.name(),
            role=random.choice(roles),
            exp=random.randint(1, 30),
            skin=random.choice(skins)
        )

        session.add(player)
        session.commit()

        players.append(player)

    worlds = []
    world_names = [
        "Infested", "Funland 3", "Minechester City", "Celestial Castle", "Mega Sky Grid,"
        "Wild West", "11 Ways To Die", "Raft Survival", "The Maze Runner Trails", 
        "Communicate 2", "Amberlight City Apocalypse", "A Modern House", "Star Wars Space World",
        "Escape Room", "Diamond Sword RPG", "Skyblock Luckyblocks"
        ]
    for name in world_names:
        world = World(
            name=name,
            seed=random.randint(100000, 999999),
            spawn=random.randint(-100, 100),
            player_count=random.randint(2, 8)
        )

        session.add(world)
        session.commit()

        worlds.append(world)

    servers = []
    server_names=["tm.mc-complex.com", "rln.rocks"]
    for world in worlds:
        for i in range(world.player_count):
            player = random.choice(players)
            server_name = random.choice(server_names)

            server = Server(
                server_name=server_name,
                server_ip=(server_names.index(server_name) + 38490),
                player_id=player.id,
                world_id=world.id
            )
            
            servers.append(server)

    session.bulk_save_objects(servers)
    session.commit()
    session.close()