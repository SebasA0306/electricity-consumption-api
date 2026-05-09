import pandas as pd

# Leer dataset
df=pd.read_csv("data/raw/electricity_consumption.csv")

# Explorar datos
print(df.head())

print(df.info())

# Valores nulos
print(df.isnull().sum())

# Cantidad antes de limpiar
print("Antes:", len(df))

# Limpiar datos
df=df.dropna()

#Cantidad después
print("Después:",len(df))

# Convertir timestamp
df["timestamp"]=pd.to_datetime(df["timestamp"])

#Crear nuevas columnas
df["hour"]=df["timestamp"].dt.hour
df["day"]=df["timestamp"].dt.day_name()

#Filtrar consumos altos
high_consumption=df[df["consumption_kwh"] > 5]
print(high_consumption.head())

#Guardar dataset limpio
df.to_csv("data/processed/cleaned_electricity_data.csv",index=False)
print("Dataset limpio guardado correctamente")