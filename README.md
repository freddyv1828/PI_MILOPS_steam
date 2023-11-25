![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)

# PI_MILOPS_steam

Este proyecto simula el rol de un MLOps Engineer, es decir, la combinación de un Data Engineer y Data Scientist, para la plataforma multinacional de videojuegos Steam. Para su desarrollo, se entregan unos datos y se solicita un Producto Mínimo Viable que muestre una API deployada en un servicio en la nube y la aplicación de un modelo de Machine Learning.

## Datos

Para este proyecto se proporcionaron tres archivos JSON:

* **australian_user_reviews.json** es un dataset que contiene los comentarios que los usuarios realizaron sobre los juegos que consumen, además de datos adicionales como si recomiendan o no ese juego, emoticones de gracioso y estadísticas de si el comentario fue útil o no para otros usuarios. También presenta el id del usuario que comenta con su url del perfil y el id del juego que comenta.

* **australian_users_items.json** es un dataset que contiene información sobre los juegos que juegan todos los usuarios, así como el tiempo acumulado que cada usuario jugó a un determinado juego.

* **output_steam_games.json** es un dataset que contiene datos relacionados con los juegos en sí, como los título, el desarrollador, los precios, características técnicas, etiquetas, entre otros datos.

## ETL

Se realizó la extracción, transformación y carga (ETL) de los tres conjuntos de datos entregados.

Los detalles del ETL se puede ver en [ETL output_steam_games](https://github.com/freddyv1828/PI_MILOPS_steam/blob/main/ETL/output_steam_games.ipynb), [ETL australian_users_items](https://github.com/freddyv1828/PI_MILOPS_steam/blob/main/ETL/users_items.ipynb) y [ETL australian_user_reviews](https://github.com/freddyv1828/PI_MILOPS_steam/blob/main/ETL/user_reviews.ipynb)

## Feature engineering

Se logro aplicar un análisis de sentimiento a los reviews de los usuarios. Para ello se creó una nueva columna llamada 'sentiment_analysis' que reemplaza a la columna que contiene los reviews donde clasifica los sentimientos de los comentarios con la siguiente escala:

* 0 si es malo,
* 1 si es neutral o esta sin review
* 2 si es positivo.

Todos los detalles del desarrollo se pueden ver en la Jupyter Notebook [01d_Feature_eng](https://github.com/freddyv1828/PI_MILOPS_steam/blob/main/Feature%20Engineering/feature_engineering.ipynb).

## EDA
Se realizó el EDA a los tres conjuntos de datos sometidos a ETL. Para ello se utilizó la librería Pandas para la manipulación de los datos y las librerías Matplotlib y Seaborn para la visualización.
El desarrollo de este análisis se encuentra en la Jupyter Notebook [EDA](https://github.com/freddyv1828/PI_MILOPS_steam/blob/main/EDA/Eda.ipynb)

## Modelo de aprendizaje automático

En el primer caso, el modelo tiene una relación ítem-ítem, esto es, se toma un juego y en base a que tan similar es ese juego con el resto de los juegos se recomiendan similares. En el segundo caso, el modelo aplicar un filtro usuario-juego, es decir, toma un usuario, encuentra usuarios similares y se recomiendan ítems que a esos usuarios similares les gustaron.


El desarrollo para la creación de los dos modelos se presenta en la Jupyter Notebook [04_Modelo_recomendacion](https://github.com/freddyv1828/PI_MILOPS_steam/blob/main/Funciones/recomendacion_juego.ipynb).

## Desarrollo API

Para el desarrolo de la API se decidió utilizar el framework FastAPI. creando las siguientes funciones: [Funciones](https://github.com/freddyv1828/PI_MILOPS_steam/tree/main/Funciones)

## Deployment

Para el deploy de la API se seleccionó la plataforma Render

El servicio se encuentra corriendo en el siguiente enlace : [https://pi-steam-milops.onrender.com]


