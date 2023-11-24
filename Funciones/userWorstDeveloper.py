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
    games_recommend = df[df["reviews_recommend"]== False & df["sentiment_analysis"]== 1]
    
    developer_recommend = games_recommend["developer"].value_counts().reset_index()
    developer_recommend.columns = ["developer", "recommend_count"]
    
    # Ordenamos
    top_developer = developer_recommend.nlargest(3, "recommend_count")
    top_developer.sort_values("recommend_count", ascending=False)
    
    resultado = [{"Puesto {}: {}".format(i + 1, row['developer']): row['recommend_count']} for i, row in top_developer.iterrows()] 
    
    return resultado

def presentacion():
    '''
    Genera una página de presentación HTML para la API Steam de consultas de videojuegos.
    
    Returns:
    str: Código HTML que muestra la página de presentación.
    '''
    return '''
    <html>
        <head>
            <title>API Steam</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                p {
                    color: #666;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>API de consultas de videojuegos de la plataforma Steam</h1>
            <p>Bienvenido a la API de Steam donde se pueden hacer diferentes consultas sobre la plataforma de videojuegos.</p>
            <p>INSTRUCCIONES:</p>
            <p>Escriba <span style="background-color: lightgray;">/docs</span> a continuación de la URL actual de esta página para interactuar con la API</p>
            <p> Visita mi perfil en <a href="https://www.linkedin.com/in/freddy-python-developer/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin"></a></p>
            <p> El desarrollo de este proyecto esta en <a href="https://github.com/freddyv1828/PI_MILOPS_steam.git"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github"></a></p>
        </body>
    </html>
    '''