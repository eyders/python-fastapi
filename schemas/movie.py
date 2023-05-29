'''Schema Movie (DTO)'''
from typing import Optional
from pydantic import BaseModel, Field


class Movie(BaseModel):
    '''Modelo'''
    id: Optional[int] = None
    title: str = Field(max_length=15, min_length=5)
    overview: str = Field(max_length=100, min_length=15)
    year: int = Field(le=2022)
    rating: float = Field(le=10, ge=1)
    category: str = Field(min_length=5, max_length=15)

    class Config:
        '''Cofiguracion de valores por defecto'''
        schema_extra = {
            'example': {
                "id": 1,
                "title": "Mi película",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 9.8,
                "category": "Acción"
            }
        }
