import pandas as pd
from fastapi import FastAPI
from Funciones.play_time_genre import playTimeGenre
from Funciones.sentiment_analysis import sentiment_analysis
from  Funciones.user_for_genre import user_for_genre
from Funciones.userRecommend import userRecomend
from Funciones.userWorstDeveloper import userWorkstDeveloper

app = FastAPI()


# Endpoint 1

@app.get("/playTimeGenre/{genero}")
def get_playTimeGenre(genero: str):
    
    '''Ingresa el Nombre de un Genero de videojuegos y veras el año con horas mas jugadas para dicho genero. 

        Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}
    
    '''
    result = playTimeGenre(genero)
    
    return result

# Endpoint 2

@app.get("/userForGenre/{genero}")
def get_userForGenre(genero: str):
    
    '''Ingresa el Nombre de un Genero de videojuegos y veras el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año. 

        Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, 
        {Año: 2011, Horas: 23}]}
    
    '''
    
    result = user_for_genre(genero)
    
    return result

# Endpoint 3

@app.get("/userRecommend/{año}")
def get_userRecommend(año: int):
    
    '''Ingresa un año y veras el top 3 de juegos MÁS recomendados por los usuarios para el año dado 

        Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
    
    '''
    
    result = userRecomend(año)
    
    return result

# Endpoint 4

@app.get("/usersWorstDeveloper/{año}")
def get_usersWorstDeveloper(año: int):
    
    '''Ingresa un año y veras el top 3 de de desarrolladoras con juegos menos recomendados por los usuarios para el año dado 

        Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
    
    '''
    
    result = userWorkstDeveloper(año)
    
    return result

@app.get("/sentiment_analysis/{desarrolladora}")
def get_sentiment_analysis(desarrolladora: str):
    
    '''Ingresa un el nombre de una empresa desarrolladora y veras la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor. 

        Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}
    
    '''
    
    result = sentiment_analysis(desarrolladora)
    
    return result