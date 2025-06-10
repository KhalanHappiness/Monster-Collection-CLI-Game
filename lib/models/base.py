from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///monster_collection.db"

#connects to the SQLite database file monster_collection.db.
engine =  create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)

#creates a base class that all your ORM models will inherit from.
Base = declarative_base()
