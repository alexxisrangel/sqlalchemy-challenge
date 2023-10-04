import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, request

#################################################
# Database Setup
#################################################
# Engine creation for hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)


# Save references to each table
Station = Base.classes.station

Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """Welcome! Here is a list of databases ready to be explored: """
    return(
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation_past_year<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/measurement<br/>"
        f"/api/v1.0/tobs_for_most_active_station<br/>"
        f"/api/v1.0/data"
    )

#app route for precipitaion
@app.route("/api/v1.0/precipitation_past_year")
def precipitaion():
    
    #Create a session to DB
    session = Session(engine)
    
    results = session.query(Measurement.date, Measurement.prcp).\
                            filter(Measurement.date > '2016-08-22').\
                            order_by(Measurement.date).all()
    session.close()
    
    #Creating the Date dictionary with prcp as value
    prcp_data = []
    for date , prcp in results:
        date_dict = {} 
        date_dict["date"] = date
        date_dict["prcp"] = prcp
        prcp_data.append(date_dict)
    
    return jsonify(prcp_data)

@app.route("/api/v1.0/stations")
def stations():
    
    #Create session to DB 
    session = Session(engine)
    
    #Creating query for entire station table 
    results = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()
    
    session.close()

    all_stations = []
    for station, name, latitude, longitude, elevation in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        station_dict["latitude"] = latitude
        station_dict["longitude"] = longitude
        station_dict["elevation"] = elevation
        all_stations.append(station_dict)

    return jsonify(all_stations)


@app.route("/api/v1.0/measurement")
def measurements():

    #Create station to DB
    session = Session(engine)

    #Creating query for entire measurement DB
    results = session.query(Measurement.station, Measurement.date, Measurement.prcp).all()

    session.close()

    all_measurements = []
    for station, date, prcp in results:
        measurements_dict = {}
        measurements_dict["station"] = station
        measurements_dict["date"] = date
        measurements_dict["prcp"] = prcp
        all_measurements.append(measurements_dict)

    return jsonify(all_measurements)



@app.route("/api/v1.0/tobs_for_most_active_station")
def most_active_stations():

    session = Session(engine)

    results = session.query(Measurement.date,Measurement.tobs).\
                            filter(Measurement.date > '2016-08-22').\
                            filter(Measurement.station == 'USC00519281').\
                            order_by(Measurement.date).all()

    session.close()

    most_recent_weather = []
    for date, tobs in results:
        date_and_temp_dict = {}
        date_and_temp_dict["date"] = date
        date_and_temp_dict["tobs"] = tobs
        most_recent_weather.append(date_and_temp_dict)
    
    return jsonify(most_recent_weather)

@app.route("/api/v1.0/data")
def start_date_query():

    #this is to get the start and end query parameters from the request 
    start_date = request.args.get('start')
    end_date = request.args.get('end')

    session = Session(engine)

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).\
        filter(Measurement.date <= end_date).all()
    

    session.close()

    #Extracting values from results 
    tmin = results[0][0]
    tavg = results[0][1]
    tmax = results[0][2]

    temp_dict = {
        'TMIN': tmin,
        'TAVG': tavg,
        'TMAX': tmax
     }
                          
    return jsonify(temp_dict)




if __name__ == '__main__':
    app.run(debug=True)
   
