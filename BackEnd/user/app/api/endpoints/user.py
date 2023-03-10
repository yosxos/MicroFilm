from api.models.User_model import UserOut,UserIn
from api.models.Movie_model import MovieIn
from fastapi import APIRouter, Depends, HTTPException, status
from databases import Database
DATABASE_URL = 'postgresql://postgres:198650@localhost/movie_app_db'
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
async def get_user_group(user_id: int):
    query="SELECT m.name FROM movies m INNER JOIN user_movie um ON m.id=um.movie_id WHERE um.user_id=:user_id"
    values={"user_id": user_id}
    movies= await database.fetch_all(query=query, values=values)
    return movies

@router.post('/{user_id}/Movies/{movie_id}')
async def add_user_movie(user_id: int, movie_id: int,movie: MovieIn):
    query="INSERT INTO user_movie (user_id, movie_id,liked,watch) VALUES (:user_id, :movie_id, :liked, :watch)"
    values={"user_id": user_id, "movie_id": movie_id ,"liked": movie.liked, "watch": movie.watched}
    await database.execute(query=query, values=values)
    return "Movie added"

@router.delete('/{user_id}/Movies/{movie_id}')
async def delete_user_movie(user_id: int, movie_id: int):
    query="DELETE FROM user_movie WHERE user_id=:user_id AND movie_id=:movie_id"
    values={"user_id": user_id, "movie_id": movie_id}
    await database.execute(query=query, values=values)
    return "Movie deleted"

@router.put('/{user_id}/Movies/{movie_id}')
async def update_user_movie(user_id: int, movie_id: int,movie: MovieIn):
    query="UPDATE user_movie SET liked=:liked, watch=:watch WHERE user_id=:user_id AND movie_id=:movie_id"
    values={"user_id": user_id, "movie_id": movie_id ,"liked": movie.liked, "watch": movie.watched}
    await database.execute(query=query, values=values)
    return "Movie updated"