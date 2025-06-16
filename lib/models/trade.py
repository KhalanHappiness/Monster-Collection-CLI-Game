from sqlalchemy import Column, Integer, String
from .base import Base

class Trade(Base):
    __tablename__ = 'trades'
    id = Column(Integer, primary_key=True)
    from_player = Column(Integer)
    to_player = Column(Integer)
    offered_monsters = Column(String)
    requested_monsters = Column(String)
    status = Column(String, default="pending")