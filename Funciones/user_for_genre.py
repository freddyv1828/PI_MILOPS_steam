import pandas as pd

# def UserForGenre( genero: str ) : Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

# Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas : 23}]}

# Cargamos la data

ruta = "Funciones/data/user_for_genre.parquet"

df_user_genre = pd.read_parquet(ruta)

# Creamos la funcion user_for_genre

def user_for_genre(genero: str):
    df = df_user_genre[df_user_genre["genres"].str.contains(genero, case=False, na=False)]
    df_result = df.groupby(["user_id", "year"])["playtime_forever"].sum().reset_index()
    max_user = df_result.iloc[df_result["playtime_forever"].idxmax()] # type: ignore
    
    acumu = df_result.groupby("year")["playtime_forever"].sum().reset_index()
    acumu = acumu.rename(columns={"playtime_forever": "hours"})
    acumu_list = acumu.to_dict(orient="records")
    
    return {"Usuario con más horas jugadas para el género " + genero: max_user['user_id'], "Horas jugadas": acumu_list}

