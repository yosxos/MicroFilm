
from sqlalchemy import (Column, Integer, MetaData, String, Table, Float, create_engine, ARRAY)

from databases import Database

DATABASE_URL = 'postgresql://postgres:198650@localhost/movie_app_db'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('overview', String(250)),
    Column('runtime',Integer),
    Column('note_average',Float),
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('email', String(250)),
    Column('token', String(1024)),
    Column('password', String(1024))
)


database = Database(DATABASE_URL)