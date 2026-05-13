import pandas as pd

#Leer datos procesados
df=pd.read_csv("data/processed/cleaned_electricity_data.csv")

#Consumo total por dispositivo
device_consumption = df.groupby("device")["consumption_kwh"].sum()


#Ordenar ranking
device_consumption = device_consumption.sort_values(ascending=False)

#Top3 dispositivos
top_3=device_consumption.head(3)


#Consumo promedio por hora
hourly_consumption = df.groupby("hour")["consumption_kwh"].mean()


#Hora pico
peak_hour = hourly_consumption.idxmax()


#Promedio por dispositivo
average_consumption = df.groupby("device")["consumption_kwh"].mean()

#Consumos extremos
extreme_consumption = df[df["consumption_kwh"]>6]


#Exportar resumen
summary=device_consumption.reset_index()

summary.columns=["device","total_consumption"]

summary.to_csv("outputs/device_consumption_summary.csv",index=False)

print("\nAnálisis completado")