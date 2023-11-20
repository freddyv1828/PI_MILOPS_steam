import pandas as pd

# def PlayTimeGenre( genero: str ) : Debe devolver añocon más horas jugadas para dicho género.

# Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

# Cargamos la data necesaria

ruta = "Funciones/data//playtime_genres.parquet"

df_playtime_genre = pd.read_parquet(ruta)

# Creamos la funcion 

def playTimeGenre(genero: str):
    df = df_playtime_genre[df_playtime_genre["genres"].str.contains(genero, case=False, na=False)]
    df_result = df.groupby("year")["playtime_forever"].sum().reset_index()
    max_year = df_result.iloc[df_result["playtime_forever"].idxmax()] # type: ignore
    
    return {"Año con más horas jugadas para el género " + genero: max_year["year"], "Horas jugadas": max_year["playtime_forever"]}

