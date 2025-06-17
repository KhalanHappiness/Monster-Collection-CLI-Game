from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class PlayerMonster(Base):
    __tablename__ = 'player_monsters'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    species_id = Column(Integer, ForeignKey('monster_species.id'))
    level = Column(Integer, default=1)
    current_hp = Column(Integer)
    experience = Column(Integer, default=0)

    player = relationship('Player', back_populates='monsters')
    species = relationship('MonsterSpecies', back_populates='player_monsters')

    def __repr__(self):
        return f"<PlayerMonster(id={self.id}, player_id={self.player_id}, species='{self.species.name}', level={self.level}, hp={self.current_hp})>"