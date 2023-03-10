from fastapi import FastAPI, HTTPException, Depends, Request
from databases import Database
from api.endpoints import user
from api.endpoints.user import database
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(user.router)