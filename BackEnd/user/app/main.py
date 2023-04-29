from fastapi import FastAPI
from databases import Database
from api.endpoints import user
from api.endpoints.user import database
import uvicorn
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(user.router)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)