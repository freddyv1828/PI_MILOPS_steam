import pandas as pd
import json

# Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
# Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

ruta = "Funciones/data/userRecommend.parquet"

df_userRecommend = pd.read_parquet(ruta) 

# Creamos la funcion

def userRecomend(año: int):
    games_year = df_userRecommend[df_userRecommend["year"] == año]
    recommends = games_year[games_year["reviews_recommend"]== True & games_year["sentiment_analysis"]== 2]
    
    # Agrupamos por juego recomendados
    games = recommends["title"].value_counts().reset_index()
    games.columns = ["games", "recommend_count"]
    
    # Ordenamos y obtenemos el top3
    top_games = games.nlargest(3, "recommend_count")
    
    resultado = [{"Puesto {}: {}".format(i + 1, row['games']): row['recommend_count']} for i, row in top_games.iterrows()] 
    
    return resultado

print(df_userRecommend)