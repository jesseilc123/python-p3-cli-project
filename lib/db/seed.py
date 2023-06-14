from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Player

from faker import Faker
import random

if __name__ == '__main__':
    engine = create_engine("sqlite:///minecraft_model.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Player).delete()

    fake = Faker()