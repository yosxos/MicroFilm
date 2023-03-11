from api.models.user_login_model import User
from fastapi import APIRouter, HTTPException, Depends, Request
from databases import Database
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException


DATABASE_URL = 'postgresql://postgres:198650@localhost/movie_app_db'
database=Database(DATABASE_URL)
router = APIRouter(
    prefix="/login",
    tags=["login"],
)
@router.post('/')
async def login(user: User, Authorize: AuthJWT = Depends()):
    user_in_db = await getUser(user)
    if(user_in_db==None):
        raise HTTPException(status_code=404, detail="User not found")
    elif(user_in_db['password']!=user.password):
        raise HTTPException(status_code=401, detail="Wrong password")
    
    access_token = Authorize.create_access_token(subject=user.email)
    await InsertToken(user, access_token)
    return {"access_token": access_token}

async def InsertToken(user: User, token: str):
    query="UPDATE users SET token=:token WHERE email=:email"
    values={"email": user.email, "token": token}
    await database.execute(query=query, values=values)

async def getUser(user:User):
    query="SELECT * FROM users WHERE email=:email"
    values={"email": user.email}
    result=await database.fetch_one(query=query, values=values)
    return result