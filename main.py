'''Working with FastAPI'''
from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router


app = FastAPI()
app.title = 'Mi aplicacion con FastAPI'  # Titulo en a documentacion
app.version = '0.0.1'  # Version en la documentacion.

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)
