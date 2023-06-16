from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer(), primary_key=True)

    user_name = Column(String())
    role = Column(String())
    exp = Column(Integer())
    skin = Column(String())

    servers = relationship("Server", back_populates="player", cascade="all, delete-orphan")
    worlds = association_proxy("servers", "world", creator=lambda wrld: Server(world=wrld))

    def __repr__(self):
        return f"Player(id={self.id}, " + \
            f"user_name={self.user_name}, " + \
            f"role={self.role}, " + \
            f"exp={self.exp}, " + \
            f"skin={self.skin})"

class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer(), primary_key=True)

    server_name = Column(String())
    server_ip = Column(Integer())

    player_id = Column(Integer(), ForeignKey("players.id"))
    world_id = Column(Integer(), ForeignKey("worlds.id"))

    player = relationship("Player", back_populates="servers")
    world = relationship("World", back_populates="servers")

    def __repr__(self):
        return f"Server(id={self.id}, " + \
            f"server_name={self.server_name}, " + \
            f"server_ip={self.server_ip}, " + \
            f"player_id={self.player_id}, " + \
            f"world_id={self.world_id})"
    
class World(Base):
    __tablename__ = "worlds"

    id = Column(Integer(), primary_key=True) 

    name = Column(String())
    seed = Column(Integer())
    spawn = Column(Integer())
    player_count = Column(Integer())

    servers = relationship("Server", back_populates="world", cascade="all, delete-orphan")
    players = association_proxy("servers", "player", creator=lambda plyr: Server(player=plyr))

    def __repr__(self):
        return f"World(id={self.id}, " + \
            f"name={self.name}, " + \
            f"seed={self.seed}, " + \
            f"spawn={self.spawn}, " + \
            f"player_count={self.player_count})"
