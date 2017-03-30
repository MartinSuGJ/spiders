# -*- coding: utf-8 -*-

# Define your models here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

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


class Movies(Base):
    """Sqlalchemy movies model"""
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    movie_type_id = Column('movie_type_id', String)
    movie_type = Column('movie_type', String)
    movie_title = Column('movie_title', String)
    movie_url = Column('movie_url', String)
    movie_cover_url = Column('movie_cover_url', String)
    movie_rank = Column('movie_rank', String)
    movie_id = Column('movie_id', String)
    movie_region = Column('movie_region', String)
    movie_actors = Column('movie_actors', String)
    movie_release_date = Column('movie_release_date', String)
    movie_vote_count = Column('movie_vote_count', String)
