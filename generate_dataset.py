import pandas as pd
import random
from datetime import datetime, timedelta

#Lista de dispositivos
devices=["Refrigerator", "Air Conditioner", "Washing Machina", "Television", "Computer"
        , "Microwave", "Fan", "Heater"]

#Lista para almacenar registros
data= []

#Fecha inicial
start_date= datetime(2025,1,1)

#Generar 10.000 registros
for i in range(10000):
    timestamp = start_date + timedelta(minutes=i)
    device=random.choice(devices)
    voltage = round(random.uniform(110,240),2)
    current = round(random.uniform(0.5,30),2)
    power = round(voltage*current,2)
    consumption_kwh=round(power/1000,2)
    
    data.append([timestamp,device,voltage, current,power, consumption_kwh])

#Crear DataFrame
df=pd.DataFrame(data,columns=["timestamp","device","voltage","current","power_watts","consumption_kwh"])

#Introducir algunos valores nulos
for _ in range(50):
    random_index = random.randint(0,9999)
    df.loc[random_index, "voltage"]=None

#Guardar CSV
df.to_csv("data/raw/electricity_consumption.csv", index=False)
print("Dataset generado correctamente")