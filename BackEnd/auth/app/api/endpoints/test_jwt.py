from fastapi import APIRouter, HTTPException, Depends, Request
from databases import Database
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException



router = APIRouter(
    prefix="/test_jwt",
    tags=["test_jwt"],
)
@router.get('/')
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return {"user": current_user, 'data': 'jwt test works'}  