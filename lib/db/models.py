from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer(), primary_key=True)

    user_name = Column(String())
    role = Column(String())
    exp = Column(Integer())
    skin = Column(String())

    servers = relationship("Server", backref=backref("player"))

    def __repr__(self):
        return f"User name: {self.user_name}" + \
            f"Role: {self.role}" + \
            f"Experience: {self.exp}" + \
            f"Skin: {self.skin}"

class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer(), primary_key=True)

    server_name = Column(String())
    server_ip = Column(Integer())

    player_id= Column(Integer(), ForeignKey("players.id"))
    world_id = Column(Integer(), ForeignKey("worlds.id"))

    def __repr__(self):
        return f"Server: {self.id}" + \
            f"Server Name: {self.server_name}" + \
            f"Server IP: {self.server_ip}"
    
class Worlds(Base):
    __tablename__ = "worlds"

    id = Column(Integer(), primary_key=True) 

    name = Column(String())
    seed = Column(Integer())
    spawn = Column(Integer())
    player_count = Column(Integer())

    servers = relationship("Server", backref=backref("world"))

    def __repr__(self):
        return f"World: {self.id}" + \
            f"Name: {self.name}" + \
            f"Seed: {self.seed}" + \
            f"Spawn: {self.spawn}" + \
            f"Player count: {self.player_count}"

