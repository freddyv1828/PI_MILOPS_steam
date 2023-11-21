import pandas as pd
import json

# UsersWorstDeveloper( año : int ): Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. 
# (reviews.recommend = False y comentarios negativos)
# Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

# Traemos la data
ruta = "Funciones/data/userWorstDeveloper.parquet"

# Abrimos el dataset
df_userWorstDeveloper = pd.read_parquet(ruta)

# Creamos la funcion

def userWorkstDeveloper(año: int):
    df = df_userWorstDeveloper[df_userWorstDeveloper["year"]== año]
    #filtramos con comenntarios negativos
    games_recommend = df[(df["reviews_recommend"]== False) & (df["sentiment_analysis"]== 1)]
    
    developer_recommend = games_recommend["developer"].value_counts().reset_index()
    developer_recommend.columns = ["developer", "recommend_count"]
    
    # Ordenamos
    top_developer = developer_recommend.nlargest(3, "recommend_count")
    top_developer.sort_values("recommend_count", ascending=False)
    
    resultado = [{"Puesto {}: {}".format(i + 1, row['developer']): row['recommend_count']} for i, row in top_developer.iterrows()] # type: ignore
    
    return json.dumps(resultado)

pr = userWorkstDeveloper(2014)
print(pr)