# funciones
import pandas as pd
import datetime as dt
import re
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Verificar tipo de dtos de los dataframe
def verificar_datos(df):
    # Comprobamos que el dataframe sea valido
    if not isinstance(df, pd.DataFrame):
        raise ValueError("El parámetro df, debe ser un dataframe de pandas")
    
    # Obtenemos un resumen de tipos de datos y valores nulos 
    resume = {"columna": [], "tipo_dato": [], "datos_nulos": [],
              "porcentaje_nulos": [], "porcentaje_no_nulos": []}
    
    for colum in df.columns:
        no_nulos = (df[colum].count()/len(df)) * 100
        # Advertimos si la columna tiene valores nulos
        if df[colum].isnull().sum():
            print(f"Advertencia: la columna {colum}, tiene valores nulos")
            
        resume["columna"].append(colum)
        resume["tipo_dato"].append(df[colum].apply(lambda x: type(x)).unique())
        resume["datos_nulos"].append(df[colum].isnull().sum())
        resume["porcentaje_nulos"].append(round(100-no_nulos, 2))
        resume["porcentaje_no_nulos"].append(round(no_nulos, 2))
        
    salida = pd.DataFrame(resume)
    return salida

# Función para encontrar valores duplicados
def valores_duplicados(df, columnas):
    # Se filtran las filas duplicadas
    duplicated_rows = df[df.duplicated(subset = columnas, keep = False)]
    
    # Numero de filas duplicadas
    numero_duplicados = duplicated_rows.shape[0]
    
    return duplicated_rows

# Funcion para mostrar valores nulos por columna
def valores_nulos_columna(df, columna):
    # Obtenemos los valores nulos de la columna
    nulos = df[columna].isnull()
    
    # Creamos un dataframe con los valores nulos
    df_nulos = df[nulos]
    
    # Añadimos el indice 
    df_nulos["index"] = df_nulos.index
    
    return df_nulos

# Funcion para extraer el año de una fecha en formato yy-mm-dd
def funcion_anio(fecha):
     if pd.notna(fecha):
        if re.match(r'^\d{4}-\d{2}-\d{2}$', fecha):
            return fecha.split('-')[0]
        return np.nan
    
# Funcion para convertir todos los datos a flotante
def conver_foltante(value):
    # Verificamos si el valor e nulo
    if pd.isna(value):
        return 0.0
    # Verificamos si el valor es un numero
    if not isinstance(value, (float, int)):
        return 0.0
    return float(value)

# Formatear fecha
def formatear_fecha(cadena_fecha):
    match = re.search(r'(\w+\s\d{1,2},\s\d{4})', cadena_fecha)
    if match:
        fecha_str = match.group(1)
        try:
            fecha_dt = pd.to_datetime(fecha_str)
            return fecha_dt.strftime('%Y-%m-%d')
        except:
            return 'Fecha inválida'
    else:
        return 'Formato inválido'
    

# Resume de porcentajes
def resumen_cant_porcentaje(df, columna, decimales=2):
  
    # Verifica que la columna exista
    if columna not in df.columns:
        raise ValueError(f'La columna "{columna}" no existe en el DataFrame.')

    # Cuanta la cantidad de True/False luego calcula el porcentaje
    counts = df[columna].value_counts()
    percentages = round(100 * counts / len(df), decimales)

    # Crea un dataframe con el resumen
    df_results = pd.DataFrame({
        "Cantidad": counts,
        "Porcentaje": percentages
    })

    return df_results

# Clasificacion
def clasificacion(row):
  
    if row["sentiment_analysis"] == 0 and not row["reviews_recommend"]:
        return 1
    elif row["sentiment_analysis"] == 0 and row["reviews_recommend"]:
        return 1
    elif row["sentiment_analysis"] == 1 and not row["reviews_recommend"]:
        return 2
    elif row["sentiment_analysis"] == 1 and row["reviews_recommend"]:
        return 3
    elif row["sentiment_analysis"] == 2 and not row["reviews_recommend"]:
        return 4
    elif row["sentiment_analysis"] == 2 and row["reviews_recommend"]:
        return 5
    else:
        return None
 