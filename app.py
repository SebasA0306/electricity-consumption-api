from flask import Flask
import pandas as pd

app=Flask(__name__)

df = pd.read_csv("data/processed/cleaned_electricity_data.csv")

@app.route("/")
def home():
    return{ "message": "Electricity Consumption API" }

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
