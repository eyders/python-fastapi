'''Schema de User (DTO)'''
from pydantic import BaseModel


class User(BaseModel):
    '''Clase User'''
    email: str
    password: str
