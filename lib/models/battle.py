from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base

class Battle(Base):
    __tablename__ = 'battles'
    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer)
    player2_id = Column(Integer)
    result = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
