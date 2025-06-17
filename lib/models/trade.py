from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Trade(Base):
    __tablename__ = 'trades'
    id = Column(Integer, primary_key=True)
    from_player = Column(Integer, ForeignKey('players.id'))
    to_player = Column(Integer, ForeignKey('players.id'))
    offered_monsters = Column(String)
    requested_monsters = Column(String)
    status = Column(String, default="pending")


    from_player_rel = relationship("Player", foreign_keys=[from_player])
    to_player_rel = relationship("Player", foreign_keys=[to_player])

    def __repr__(self):
        return f"<Trade(id={self.id}, from={self.from_player}, to={self.to_player}, status='{self.status}')>"
