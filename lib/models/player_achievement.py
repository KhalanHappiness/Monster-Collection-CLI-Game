from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base



class PlayerAchievement(Base):
    __tablename__ = 'player_achievements'
    player_id = Column(Integer, ForeignKey('players.id'), primary_key=True)
    achievement_id = Column(Integer, ForeignKey('achievements.id'), primary_key=True)
    unlocked_at = Column(DateTime, default=datetime.utcnow)

    player = relationship('Player', back_populates='achievements')
    achievement = relationship('Achievement', back_populates='players')


    def __repr__(self):
        return f"<PlayerAchievement(player_id={self.player_id}, achievement_id={self.achievement_id}, unlocked_at={self.unlocked_at})>"