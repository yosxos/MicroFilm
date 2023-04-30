from api.models.User_model import UserOut,UserIn
from api.models.Movie_model import MovieIn
from fastapi import APIRouter, Depends, HTTPException, status
from databases import Database
import os
DATABASE_URL = os.getenv('DATABASE_URL')
database=Database(DATABASE_URL)

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.get("/{user_id}",response_model=UserOut)
async def get_user(user_id: int):
    """
    Get a user by id

    Args:
        user_id (int): The id of the user

    Returns:
        UserOut: The user with the given id
    """
    query = "SELECT * FROM users WHERE id = :user_id"
    values = {"user_id": user_id}
    user = await database.fetch_one(query=query, values=values)
    return user

@router.post("/create")
async def create_user(user: UserIn):
    """
    Create a new user

    """
    query = "INSERT INTO users (email, password, name) VALUES (:email, :password, :name)"
    values = {"email": user.email, "password": user.password, "name": user.name}
    await database.execute(query=query, values=values)
    return "User created"

@router.put("/update/{user_id}")
async def update_user(user_id: int, user: UserIn):
    query="UPDATE users SET email=:email, password=:password, name=:name WHERE id=:user_id"
    values={"email": user.email, "password": user.password, "name": user.name, "user_id": user_id}
    await database.execute(query=query, values=values)
    return "User updated"

@router.delete("/delete/{user_id}")
async def delete_user(user_id: int):
    """
    Delete a user by id

    Args:
        user_id (int):  The id of the user
    """
    query="DELETE FROM users WHERE id=:user_id"
    values={"user_id": user_id}
    await database.execute(query=query, values=values)
    return "User deleted"

@router.get('/{user_id}/Movies')
async def get_user_movies(user_id: int):
    """
    Get all movies of a user

    Args:
        user_id (int): The id of the user

    Returns:
        _type_: Movie
    """
    query="SELECT m,um.watch,um.like FROM movies m INNER JOIN user_movie um ON m.id=um.movie_id WHERE um.user_id=:user_id"
    values={"user_id": user_id}
    movies= await database.fetch_all(query=query, values=values)
    return movies

@router.post('/{user_id}/Movies/add')
async def add_user_movie(user_id: int,movie: MovieIn):
    """ 
    Add a movie to a user

    Args:
        user_id (int): The id of the user
        movie_id (int): The id of the movie
        movie (MovieIn): The movie to add

    """
    query="INSERT INTO user_movie (user_id, movie_id, like, watch) SELECT :user_id, :movie_id, :like, :watch WHERE NOT EXISTS (   SELECT 1  FROM user_movie   WHERE user_id = :user_id AND movie_id = :movie_id)"

    values={"user_id": user_id, "movie_id": movie.movie_id ,"like": movie.liked, "watch": movie.watched}
    await database.execute(query=query, values=values)
    return "Movie added"

@router.delete('/{user_id}/Movies/delete/{movie_id}')

async def delete_user_movie(user_id: int, movie_id: int):
    """
    Delete a movie from a user

    Args:
        user_id (int): User id
        movie_id (int): Movie id

    """
    query="DELETE FROM user_movie WHERE user_id=:user_id AND movie_id=:movie_id"
    values={"user_id": user_id, "movie_id": movie_id}
    await database.execute(query=query, values=values)
    return "Movie deleted"

@router.put('/{user_id}/Movies/update/{movie_id}')
async def update_user_movie(user_id: int,movie_id:int,movie: MovieIn):
    """
    Update a movie from a user

    Args:
        user_id (int): User id
        movie_id (int): Movie id
        movie (MovieIn): The movie to update

    Returns:
        _type_: Movie
    """
    query="UPDATE user_movie SET like=:like, watch=:watch WHERE user_id=:user_id AND movie_id=:movie_id"
    values={"user_id": user_id, "movie_id": movie.movie_id ,"like": movie.liked, "watch": movie.watched}
    await database.execute(query=query, values=values)
    return "Movie updated"

@router.get('/{user_id}/Genres')
async def get_user_genres(user_id: int):
    """
    Get all prefered genres of a user

    Args:
        user_id (int): user id
    """
    query="SELECT g.name,g.id FROM genres g INNER JOIN user_genre ug ON g.id=ug.genre_id WHERE ug.user_id=:user_id"
    values={"user_id": user_id}
    genres= await database.fetch_all(query=query, values=values)
    return genres

@router.post('/{user_id}/Genres/add')
async def add_user_genre(user_id: int, genre_id: int):
    """
    Add a genre to a user

    Args:
        user_id (int): user id
        genre_id (int): genre id
    """
    query="INSERT INTO user_genre (user_id, genre_id) SELECT :user_id, :genre_id WHERE NOT EXISTS ( SELECT 1 FROM user_genre WHERE user_id = :user_id AND genre_id = :genre_id)"
    values={"user_id": user_id, "genre_id": genre_id}
    await database.execute(query=query, values=values)
    return "Genre added"

@router.put('/{user_id}/Genres/update/{genre_id}')
async def update_user_genre(user_id: int, genre_id: int,genre_update_id: int):
    """
    Update a genre from a user

    Args:
        user_id (int): _description_
        genre_id (int): _description_

    Returns:
        _type_: _description_
    """
    query="UPDATE user_genre SET genre_id=:genre_update_id WHERE user_id=:user_id AND genre_id=:genre_id"
    values={"user_id": user_id, "genre_id": genre_id, "genre_update_id": genre_update_id}
    await database.execute(query=query, values=values)
    return "Genre updated"

@router.delete('/{user_id}/Genres/delete/{genre_id}')
async def delete_user_genre(user_id: int, genre_id: int):
    """
    Delete a genre from a user

    Args:
        user_id (int): user id
        genre_id (int): genre id
    """
    query="DELETE FROM user_genre WHERE user_id=:user_id AND genre_id=:genre_id"
    values={"user_id": user_id, "genre_id": genre_id}
    await database.execute(query=query, values=values)
    return "Genre deleted"

@router.get('/{user_id}/Groups')
async def get_user_groups(user_id: int):
    """
    Get all groups of a user

    Args:
        user_id (int): user id
    """
    query="SELECT g.name,g.id FROM group g INNER JOIN user_group ug ON g.id=ug.group_id WHERE ug.user_id=:user_id"
    values={"user_id": user_id}
    groups= await database.fetch_all(query=query, values=values)
    return groups

@router.post('/{user_id}/Groups/add')
async def add_user_group(user_id: int, group_id: int):
    """
    Add a group to a user

    Args:
        user_id (int): user id
        group_id (int): group id
    """
    query="INSERT INTO user_group (user_id, group_id) SELECT :user_id, :group_id WHERE NOT EXISTS (  SELECT 1  FROM user_group  WHERE user_id = :user_id AND group_id = :group_id)"
    values={"user_id": user_id, "group_id": group_id}
    await database.execute(query=query, values=values)
    return "Group added"

@router.put('/{user_id}/Groups/update/{group_id}')
async def update_user_group(user_id: int, group_id: int,group_update_id: int):
    """
    Update a group from a user

    Args:
        user_id (int): User id
        group_id (int): Group id
        group_update_id (int): Group id to update

    """
    query="UPDATE user_group SET group_id=:group_update_id WHERE user_id=:user_id AND group_id=:group_id"
    values={"user_id": user_id, "group_id": group_id, "group_update_id": group_update_id}
    await database.execute(query=query, values=values)
    return "Group updated"

@router.delete('/{user_id}/Groups/delete/{group_id}')
async def delete_user_group(user_id: int, group_id: int):
    """
    Delete a group from a user

    Args:
        user_id (int): user id
        group_id (int): group id
    """
    query="DELETE FROM user_group WHERE user_id=:user_id AND group_id=:group_id"
    values={"user_id": user_id, "group_id": group_id}
    await database.execute(query=query, values=values)
    return "Group deleted"