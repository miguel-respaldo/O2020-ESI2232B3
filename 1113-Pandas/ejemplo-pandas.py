import pandas as pd

nba = pd.read_csv("nbaallelo.csv")
#nba = pd.read_csv("productos.csv")

# Ver el tipo de dato de nba
#print(type(nba))

# Ver el tamaño de los registros que hay en nba
print("Tamaño de registros en NBA:", len(nba))
print("La forma de los datos (filas, columnas)", nba.shape)

# Ver las primeras 5 filas
print(nba.head())

# Configuramos para que se vean todas las columnas
pd.set_option("display.max.columns", None)

# Configuramos para que salgan solo 2 digitos decimales
pd.set_option("display.precision", 2)

# imprimimos las ultimas 5 filas
print(nba.tail())

# Imprimir la información de los datos
print(nba.info())
print("**********************")
print(nba.describe())
print("**********************")

# Ver cuantos valores hay de cadauno de entradas
print(nba["team_id"].value_counts())
print("**********************")
print(nba["fran_id"].value_counts())

# Hubo 5078 juegos en LAL (Los Angeles)
# Lakers jugo 6024 juegos
# ¿Donde más jugaron los Lakers?
print( nba.loc[nba["fran_id"] == "Lakers", "team_id"].value_counts() )
