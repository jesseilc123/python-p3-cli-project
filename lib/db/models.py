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

class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer(), primary_key=True)

    server_name = Column(String())
    server_ip = (Integer())

    def __repr__(self):
        return f"Server: {self.id}" + \
            f"Server Name: {self.server_name}" + \
            f"Server IP: {self.server_ip}"

