'''Router para User'''
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_tocken
from schemas.user import User


user_router = APIRouter()


@user_router.post('/login', tags=['Auth'])
def login(user: User):
    '''User Login'''
    if user.email == 'admin@gmail.com' and user.password == 'admin':
        token = create_tocken(user.dict())
        return JSONResponse(status_code=200, content=token)
