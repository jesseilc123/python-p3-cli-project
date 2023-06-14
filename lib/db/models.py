from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer(), primary_key=True)
    user_name = Column(String())
    role = Column(String())
    exp = Column(Integer())
    skin = Column(String())

    def __repr__(self):
        return f"User name: {self.user_name}" + \
            f"Role: {self.role}" + \
            f"Experience: {self.exp}" + \
            f"Skin: {self.skin}"



