from fastapi import FastAPI
from api.movies import movies
from api.db import metadata, database, engine
import uvicorn
from api.tmdb import main
from fastapi.middleware.cors import CORSMiddleware
metadata.create_all(engine)

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
    await main() # Call the main function from your script

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(movies, prefix='/api/v1/movies',tags=['movies'])
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)