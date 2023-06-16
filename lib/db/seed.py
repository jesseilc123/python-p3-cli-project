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
            name=fake.unique.name(),
            seed=random.randint(100000, 999999),
            spawn=[f"x:{random.randint(-100, 100)}", f"y:{random.randint(-100, 100)}", f"z:{random.randint(-100, 100)}"],
            player_count=random.randint(1, 30)
        )

        session.add(world)
        session.commit()

        worlds.append(world)