import pandas as pd
import operator

# A continuacion Cream os las funaciones para el modelos de recomendacion de ML

# Leer archivos

piv_norm = pd.read_parquet("Funciones/data/piv_norm.parquet")
user_sim_df= pd.read_parquet("Funciones/data/user_sim_df.parquet")
item_sim_df = pd.read_parquet("Funciones/data/item_sim_df.parquet")

# Creamos las funciones

# Funcion recomendacion_juego

def top_game(game):
        # Obtener la lista de juegos similares ordenados
    similar_games = item_sim_df.sort_values(by=game, ascending=False).iloc[1:6]

    count = 1
    contador = 1
    recomendaciones = {}
    
    for item in similar_games:
        if contador <= 5:
            item = str(item)
            recomendaciones[count] = item
            count += 1
            contador += 1 
        else:
            break
    return recomendaciones


# Funcion recomendacion_usuario

def similar_user_recs(user):

    # Verifica si el usuario está presente en las columnas de piv_norm (si no está, devuelve un mensaje)
    if user not in piv_norm.columns:
        return('No data available on user {}'.format(user))
    
    # Obtiene los usuarios más similares al usuario dado
    sim_users = user_sim_df.sort_values(by=user, ascending=False).index[1:11]
    
    best = []  # Lista para almacenar los juegos mejor calificados por usuarios similares
    most_common = {}  # Diccionario para contar cuántas veces se recomienda cada juego
    
    # Para cada usuario similar, encuentra el juego mejor calificado y lo agrega a la lista 'best'
    for i in sim_users:
        max_score = piv_norm.loc[:, i].max()
        best.append(piv_norm[piv_norm.loc[:, i]==max_score].index.tolist())
    
    # Cuenta cuántas veces se recomienda cada juego
    for i in range(len(best)):
        for j in best[i]:
            if j in most_common:
                most_common[j] += 1
            else:
                most_common[j] = 1
    
    # Ordena los juegos por la frecuencia de recomendación en orden descendente
    sorted_list = sorted(most_common.items(), key=operator.itemgetter(1), reverse=True)
    
    # Devuelve los 5 juegos más recomendados
    return sorted_list[:5]
        
