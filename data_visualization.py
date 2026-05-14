import pandas as pd
import matplotlib.pyplot as plt

#Leer dataset limpio
df=pd.read_csv("data/processed/cleaned_electricity_data.csv")

#Consumo por dispositivo
device_consumption = df.groupby("device")["consumption_kwh"].sum()
device_consumption = device_consumption.sort_values(ascending=False)

#Gráfico de barras
device_consumption.plot(kind="bar")
plt.title("Energy consumption by device")
plt.xlabel("Device")
plt.ylabel("Total consumption (kWh)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/charts/device_consumption.png")
plt.show()

#Consumo promedio por hora
hourly_consumption = df.groupby("hour")["consumption_kwh"].mean()

#Gráfico de línea
hourly_consumption.plot(kind="line")
plt.title("Average hourly consumption")
plt.xlabel("Hour")
plt.ylabel("Average consumption (kWh)")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/charts/hourly_consumption.png")
plt.show()

#Dispositivo con mayor consumo
top_device = device_consumption.idxmax()
print("Highest consumption device:", top_device)