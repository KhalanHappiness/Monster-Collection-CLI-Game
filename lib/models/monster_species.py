from sqlalchemy import Column, Integer, String
from .base import Base

class MonsterSpecies(Base):
    __tablename__ = 'monster_species'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    type = Column(String)
    base_hp = Column(Integer)
    base_attack = Column(Integer)
    base_defense = Column(Integer)
    rarity = Column(String)
    abilities = Column(String)
