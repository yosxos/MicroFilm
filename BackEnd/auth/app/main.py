from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints.login import router as login_router
from api.endpoints.test_jwt import router as test_jwt_router
from api.endpoints.login import database
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

app.include_router(login_router)
app.include_router(test_jwt_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)