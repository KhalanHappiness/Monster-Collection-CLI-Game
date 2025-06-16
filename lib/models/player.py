from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    money = Column(Integer, default=100)

    monsters = relationship('PlayerMonster', back_populates='player')
    achievements = relationship('PlayerAchievement', back_populates='player')
