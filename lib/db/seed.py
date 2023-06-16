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
    for i in range(5):
        player = Player(
           user_name=fake.unique.name(),
           role=fake.unique.name(),
           exp=random.randint(1, 30),
           skin=fake.unique.name()
        )

        session.add(player)
        session.commit()

        players.append(player)

    worlds = []
    for i in range(5):
        world = World(
            name=fake.name(),
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