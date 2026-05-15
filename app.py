from flask import Flask
import pandas as pd

app=Flask(__name__)

df = pd.read_csv("data/processed/cleaned_electricity_data.csv")

@app.route("/")
def home():
    return{ "message": "Electricity Consumption API" }

#Endpoint dinámico
@app.route("/device/<device_name>")
def get_device_data(device_name):
    filtered_data=df[df["device"].str.lower()==device_name.lower()]
    
    if filtered_data.empty:
        return{"error":"Device not found"},404
    
    return filtered_data.head(10).to_dict(orient="records")

@app.route("/top-devices")
def top_devices():
    ranking = df.groupby("device")["consumption_kwh"].sum()
    ranking = ranking.sort_values(ascending=False)
    return ranking.head(5).to_dict()

@app.route("/peak-hour")
def peak_hour():
    hourly_consumption =df.groupby("hour")["consumption_kwh"].mean()
    peak=hourly_consumption.idxmax()
    return {"peak_hour":int(peak)}

@app.route("/devices")
def get_devices():
    
    devices=df["device"].unique().tolist()
    
    return {"devices":devices}

@app.route("/records")
def get_records():
    
    total_records = len(df)
    
    return {"total_records":total_records}

if __name__ == "__main__":
    app.run(debug=True)
