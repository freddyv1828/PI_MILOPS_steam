import pandas as pd

# Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros 

# de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.

# Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}

# cargamos la data

ruta_items = "Funciones/data/sentiment_analysis_items.parquet"
ruta_sentiment = "Funciones/data/sentiment_analysis.parquet"

# Abrimos los dataframe

df_items = pd.read_parquet(ruta_items)
df_combined = pd.read_parquet(ruta_sentiment)

# Creamos la funcion

def sentiment_analysis(desarrolladora: str):
    # filtra juego para desarrollador dado
    games_developer = df_combined[df_combined["developer"]== desarrolladora]
    # obtiene el id de los juegos seleccionados
    game_id = games_developer["id"]
    
    items_developer = df_items[df_items["item_id"].isin(game_id)]
    
    # Obtenemos el id d los usuarios
    user_id = items_developer["user_id"]
    
    reviews_developer = df_combined[df_combined["user_id"].isin(user_id)]
    
    reviews_positive = reviews_developer[reviews_developer["reviews_recommend"] == True].shape[0]
    reviews_negative = reviews_developer[reviews_developer["reviews_recommend"]== False].shape[0]
    
    return {desarrolladora: {"Positive":reviews_positive, "Negative":reviews_negative}}

