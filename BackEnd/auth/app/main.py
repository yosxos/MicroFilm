from typing import Optional
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models import User
from databases import Database


DATABASE_URL = 'postgresql://postgres:198650@localhost/movie_app_db'
database=Database(DATABASE_URL)
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

class Settings(BaseModel):
    authjwt_secret_key: str = "my_jwt_secret"
@AuthJWT.load_config
def get_config():
    return Settings()
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

@app.post('/login')
async def login(user: User, Authorize: AuthJWT = Depends()):
    print(user)
    # if( await checkUserExists(user)==False):
    #     raise HTTPException(status_code=404, detail="User not found")
    # elif( await checkUserPassword(user)==False):
    #     raise HTTPException(status_code=401, detail="Wrong password")
    user_in_db = await getUser(user)
    if(user_in_db==None):
        raise HTTPException(status_code=404, detail="User not found")
    elif(user_in_db['password']!=user.password):
        raise HTTPException(status_code=401, detail="Wrong password")
    
    access_token = Authorize.create_access_token(subject=user.email)
    await InsertToken(user, access_token)
    return {"access_token": access_token}

@app.get('/test-jwt')
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return {"user": current_user, 'data': 'jwt test works'}    

async def InsertToken(user: User, token: str):
    query="UPDATE users SET token=:token WHERE email=:email"
    values={"email": user.email, "token": token}
    await database.execute(query=query, values=values)

async def getUser(user:User):
    query="SELECT * FROM users WHERE email=:email"
    values={"email": user.email}
    result=await database.fetch_one(query=query, values=values)
    return result