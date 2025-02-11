from flask import Flask, render_template
import pandas as pd

app = Flask("website")

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data = stations.to_html())

@app.route("/api/<station>/<date>")
def about(station, date):
    file_address = "data_small/TG_STAID"+ str(station).zfill(6) + ".txt"
    df = pd.read_csv(file_address, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10

    return {"station" : station, "date" : date, "temperature" : temperature}

@app.route("/api/<station>")
def station_data(station):
    file_address = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(file_address, skiprows=20, parse_dates=["    DATE"])
    return df.to_dict(orient="records")

@app.route("/api/yearly/<station>/<year>")
def year_data(station,year):
    file_address = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(file_address, skiprows=20, parse_dates=["    DATE"])
    df["    DATE"] = df["    DATE"].astype(str)
    yearly_data = df[df["    DATE"].str.startswith(str(year))]
    return yearly_data.to_dict(orient="records")

app.run(debug=True)