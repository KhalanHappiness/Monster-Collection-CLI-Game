from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Achievement(Base):
    __tablename__ = 'achievements'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    players = relationship('PlayerAchievement', back_populates='achievement')


    def __repr__(self):
        return f"<Achievement(id={self.id}, name='{self.name}')>"
