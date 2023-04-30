from fastapi import FastAPI
from databases import Database
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import user
from api.endpoints.user import database
import uvicorn
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:80",
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

app.include_router(user.router)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)