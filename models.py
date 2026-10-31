from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, unique = True, index = True, nullable = False)
    score = Column(Integer, default=0)


#связь с матчами (один игрок может иметь много матчей)
    matches = relationship (
        "Match", back_populates="player", cascade = "all, delete-orphan"
    )


class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key = True, index = True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable = False)
    result = Column(String, nullable=False)
    kills = Column(Integer, default = 0)
    deaths = Column(Integer, default = 0)


    player = relationship("Player", back_populates="matches")