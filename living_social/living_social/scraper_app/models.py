from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
import settings

Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_deals_table(engine):
    """"""
    Base.metadata.create_all(engine)


class Deals(Base):
    """Sqlalchemy deals model"""
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    link = Column('link', String, nullable=True)
    location = Column('location', String, nullable=True)
    original_price = Column('original_price', Integer, nullable=True)
    price = Column('price', Integer, nullable=True)
    end_date = Column('end_date', String, nullable=True)
