from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from .base import Base

class Battle(Base):
    __tablename__ = 'battles'
    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer, ForeignKey('players.id'))
    player2_id = Column(Integer, ForeignKey('players.id'))
    result = Column(String)
    date = Column(DateTime, default=datetime.utcnow)

    player1 = relationship("Player", foreign_keys=[player1_id])
    player2 = relationship("Player", foreign_keys=[player2_id])

    def __repr__(self):
        return f"<Battle(id={self.id}, player1_id={self.player1_id}, player2_id={self.player2_id}, result='{self.result}', date={self.date})>"
