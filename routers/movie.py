'''Router para Movie'''
from fastapi import APIRouter
from typing import Optional, List
from fastapi import Path, Query, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from models.movie import Movie as MovieModel
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


# Home es una etiqueta que aparece en la documentacion
@movie_router.get('/', tags=['Home'])
def message():
    '''Test'''
    return HTMLResponse('<h1>Hello world</h1>')


@movie_router.get('/movies', tags=['Movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies():
    '''Get Movies'''
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Parametros


@movie_router.get('/movies/{id}', tags=['Movies'], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=1, le=200)) -> Movie:
    '''Get Movie'''
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})

    return JSONResponse(content=jsonable_encoder(result))


# Parametros Query


@movie_router.get('/movies/', tags=['Movies'], response_model=List[Movie])
def get_movie_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    '''Get movies with query parameters'''
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(
            status_code=404,
            content={'message': f'No se encontro ninguna pelicula en la categoria: {category}'})
    return JSONResponse(content=jsonable_encoder(result))

# Metodo POST


@movie_router.post('/movies', tags=['Movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie):
    '''Creat Movie'''
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={'message': 'Se ha registrado la pelicula'})

# Modificaciones con PUT


@movie_router.put('/movies/{id}', tags=['Movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie):
    '''Modificar Registro'''
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})

    MovieService(db).update_movie(id, movie)

    return JSONResponse(status_code=201, content={'message': 'Se ha modificado la pelicula'})

# Dellete registers


@movie_router.delete('/movies/{id}', tags=['Movies'], response_model=dict, status_code=200)
def delete_movie(id: int):
    '''Eliminar registro'''
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})

    MovieService(db).delete_movie(id)

    return JSONResponse(status_code=201, content={'message': 'Se ha eliminado la pelicula'})
