from api.model.User_model import UserOut,UserIn
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
    query = "SELECT * FROM users WHERE id = :user_id"
    values = {"user_id": user_id}
    user = await database.fetch_one(query=query, values=values)
    return user

@router.post("/create")
async def create_user(user: UserIn):
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
    query="DELETE FROM users WHERE id=:user_id"
    values={"user_id": user_id}
    await database.execute(query=query, values=values)
    return "User deleted"

