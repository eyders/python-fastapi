'''Modulo de creacion de tokens'''
from jwt import encode, decode


def create_tocken(data: dict):
    '''Generando token'''
    token = encode(payload=data, key='my_secrete_key', algorithm='HS256')
    return token


def validate_token(token: str) -> dict:
    '''Validar token'''
    data: dict = decode(token, key='my_secrete_key', algorithms=['HS256'])
    return data
