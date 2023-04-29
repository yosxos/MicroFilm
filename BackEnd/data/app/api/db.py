from sqlalchemy.orm import relationship
from sqlalchemy import (Column, ForeignKey, Text, Boolean, ForeignKeyConstraint, Integer, MetaData, String, Table, Float, create_engine, ARRAY)
from sqlalchemy import insert, select
from databases import Database
import os
DATABASE_URL = os.getenv('DATABASE_URL')

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(250)),
    Column('overview', Text),
    Column('release_date',String(50)),
    Column('note_average',Float),
    Column('poster_path', String(1024) or None),
    Column('genres_id',ARRAY(Integer))
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(50)),
    Column('email', String(250)),
    Column('token', String(1024)),
    Column('password', String(1024))
)

group = Table(
    'group',
    metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name',String(250))
)

genre = Table(
    'genre',
    metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(250))
)

user_group = Table(
    'user_group',
    metadata,
    Column('user_id',Integer, ForeignKey('users.id'), nullable=False),
    Column('group_id', Integer, ForeignKey('group.id'),nullable=False)
)

user_genre = Table(
    'user_genre',
    metadata,
    Column('user_id',Integer, ForeignKey('users.id'), nullable=False),
    Column('genre_id', Integer, ForeignKey('genre.id'),nullable=False)
)

user_movie = Table(
    'user_movie',
    metadata,
    Column('user_id',Integer, ForeignKey('users.id'), nullable=False),
    Column('movie_id', Integer, ForeignKey('movies.id'),nullable=False),
    Column('watch',Boolean),
    Column('like',Boolean)
    
)




