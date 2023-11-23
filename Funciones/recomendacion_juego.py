import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer

# A continuacion Cream os las funaciones para el modelos de recomendacion de ML

# Leer archivos

df_games = pd.read_parquet("Datasets/steam_games_limpio.parquet")
genre_features = pd.read_parquet("Funciones/data/genre_features.parquet")

# Funcion

def recomendacion_juego(id_producto, num_recomendaciones=5):
    if id_producto not in genre_features.index:
        return {"error": "El juego no se encuentra en la base de datos."}
    # Resto del código para calcular la similitud del coseno y obtener las recomendaciones
    juego_seleccionado = np.array(genre_features.loc[id_producto].values).reshape(1, -1)
    similaridades = cosine_similarity(juego_seleccionado, genre_features)

    juegos_similares_indices = similaridades.argsort()[0][-num_recomendaciones:][::-1]
    juegos_recomendados = df_games.iloc[juegos_similares_indices, :]

    lista = [{"id": row['id'], "title": row['title']} for index, row in juegos_recomendados.iterrows()]

    return lista
        
