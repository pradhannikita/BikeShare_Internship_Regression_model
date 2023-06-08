import pickle
from flask import Flask, request, app, jsonify ,url_for, render_template
import numpy as np
from flask_cors import cross_origin

app = Flask(__name__)
model = pickle.load(open("bike_regression.pkl", "rb"))

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/predict", methods = ["GET","POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        #Temperature
        temp = float(request.form['temp_day'])

        #Humidity
        humidity = float(request.form["humidity"])

        #Season
        
        season = request.form['season']
        if(season == "Spring"):
            season_1 = 1
            season_2 = 0
            season_3 = 0
            season_4 = 0
        
        elif(season == "Summer"):
            season_1 = 0
            season_2 = 1
            season_3 = 0
            season_4 = 0

        elif(season == "Fall"):
            season_1 = 0
            season_2 = 0
            season_3 = 1
            season_4 = 0

        elif(season == "Winter"):
            season_1 = 0
            season_2 = 0
            season_3 = 0
            season_4 = 1
        else:
            season_1 = 0
            season_2 = 0
            season_3 = 0
            season_4 = 0

        weather = request.form['weather']

        if(weather == "Clear Day"):
            weather_1 = 1
            weather_2 = 0
            weather_3 = 0
            weather_4 = 0
        
        elif(weather == "Mist + Cloudy"):
            weather_1 = 0
            weather_2 = 1
            weather_3 = 0
            weather_4 = 0

        elif(weather == "Light Snow / Rain"):
            weather_1 = 0
            weather_2 = 0
            weather_3 = 1
            weather_4 = 0

        elif(weather == "Heavy Show / Rain"):
            weather_1 = 0
            weather_2 = 0
            weather_3 = 0
            weather_4 = 1
        else:
            weather_1 = 0
            weather_2 = 0
            weather_3 = 0
            weather_4 = 0

        month = request.form['month']

        if(month == "January"):
            month_1 = 1
            month_2 = 0
            month_3 = 0
            month_4 = 0
            month_5 = 0
            month_6 = 0
            month_7 = 0
            month_8 = 0
            month_9 = 0
            month_10 = 0
            month_11 = 0
            month_12 = 0

        elif(month == "February"):
            month_1 = 0
            month_2 = 1
            month_3 = 0
            month_4 = 0
            month_5 = 0
            month_6 = 0
            month_7 = 0
            month_8 = 0
            month_9 = 0
            month_10 = 0
            month_11 = 0
            month_12 = 0

        elif(month == "March"):
            month_1 = 0
            month_2 = 0
            month_3 = 1
            month_4 = 0
            month_5 = 0
            month_6 = 0
            month_7 = 0
            month_8 = 0
            month_9 = 0
            month_10 = 0
            month_11 = 0
            month_12 = 0

        elif(month == "April"):
            month_1 = 0
            month_2 = 0
            month_3 = 0
            month_4 = 1
            month_5 = 0
            month_6 = 0
            month_7 = 0
            month_8 = 0
            month_9 = 0
            month_10 = 0
            month_11 = 0
            month_12 = 0

        elif(month == "May"):
            month_1 = 0
            month_2 = 0
            month_3 = 0
            month_4 = 0
            month_5 = 1
            month_6 = 0
            month_7 = 0
            month_8 = 0
            month_9 = 0
            month_10 = 0
            month_11 = 0
            month_12 = 0

        elif(month == "June"):
            month_1 = 0
            month_2 = 0
            month_3 = 0
            month_4 = 0
            month_5 = 0
            month_6 = 1
            month_7 = 0
            month_8 = 0
            month_9 = 0
            month_10 = 0
            month_11 = 0
            month_12 = 0

        elif(month == "July"):
            month_1 = 0
            month_2 = 0
            month_3 = 0
            month_4 = 0
            month_5 = 0
            month_6 = 0
            month_7 = 1
            month_8 = 0
            month_9 = 0
            month_10 = 0
            month_11 = 0
            month_12 = 0

        elif(month == "August"):
            month_1 = 0
            month_2 = 0
            month_3 = 0
            month_4 = 0
            month_5 = 0
            month_6 = 0
            month_7 = 0
            month_8 = 1
            month_9 = 0
            month_10 = 0
            month_11 = 0
            month_12 = 0


        elif(month == "September"):
            month_1 = 0
            month_2 = 0
            month_3 = 0
            month_4 = 0
            month_5 = 0
            month_6 = 0
            month_7 = 0
            month_8 = 0
            month_9 = 1
            month_10 = 0
            month_11 = 0
            month_12 = 0

        elif(month == "October"):
            month_1 = 0
            month_2 = 0
            month_3 = 0
            month_4 = 0
            month_5 = 0
            month_6 = 0
            month_7 = 0
            month_8 = 0
            month_9 = 0
            month_10 = 1
            month_11 = 0
            month_12 = 0

        elif(month == "November"):
            month_1 = 0
            month_2 = 0
            month_3 = 0
            month_4 = 0
            month_5 = 0
            month_6 = 0
            month_7 = 0
            month_8 = 0
            month_9 = 0
            month_10 = 0
            month_11 = 1
            month_12 = 0

        elif(month == "December"):
            month_1 = 0
            month_2 = 0
            month_3 = 3
            month_4 = 0
            month_5 = 0
            month_6 = 0
            month_7 = 0
            month_8 = 0
            month_9 = 0
            month_10 = 0
            month_11 = 0
            month_12 = 1
        else:
            month_1 = 0
            month_2 = 0
            month_3 = 0
            month_4 = 0
            month_5 = 0
            month_6 = 0
            month_7 = 0
            month_8 = 0
            month_9 = 0
            month_10 = 0
            month_11 = 0
            month_12 = 0


        weekday = request.form['weekday']

        if(weekday == "Sunday"):
            weekday_0 = 1
            weekday_1 = 0
            weekday_2 = 0
            weekday_3 = 0
            weekday_4 = 0
            weekday_5 = 0
            weekday_6 = 0
        
        elif(weekday == "Monday"):
            weekday_0 = 0
            weekday_1 = 1
            weekday_2 = 0
            weekday_3 = 0
            weekday_4 = 0
            weekday_5 = 0
            weekday_6 = 0

        elif(weekday == 'Tuesday'):
            weekday_0 = 0
            weekday_1 = 0
            weekday_2 = 1
            weekday_3 = 0
            weekday_4 = 0
            weekday_5 = 0
            weekday_6 = 0

        elif(weekday == 'Wednesday'):
            weekday_0 = 0
            weekday_1 = 0
            weekday_2 = 0
            weekday_3 = 1
            weekday_4 = 0
            weekday_5 = 0
            weekday_6 = 0

        elif(weekday == "Thursday"):
            weekday_0 = 0
            weekday_1 = 0
            weekday_2 = 0
            weekday_3 = 0
            weekday_4 = 1
            weekday_5 = 0
            weekday_6 = 0

        elif(weekday == 'Friday'):
            weekday_0 = 0
            weekday_1 = 0
            weekday_2 = 0
            weekday_3 = 0
            weekday_4 = 0
            weekday_5 = 1
            weekday_6 = 0

        elif(weekday == 'Saturday'):
            weekday_0 = 0
            weekday_1 = 0
            weekday_2 = 0
            weekday_3 = 0
            weekday_4 = 0
            weekday_5 = 0
            weekday_6 = 1


        holiday = request.form['holiday']

        if(holiday == 'No'):
            holiday_0 = 1
            holiday_1 = 0
        else:
            holiday_0 = 0
            holiday_1 = 1

        workingday = request.form['workingday']

        if(workingday == 'Yes'):
            workingday_0 = 1
            workingday_1 = 0
        else:
            workingday_0 = 1
            workingday_1 = 0

        hour = request.form['hour']
        if(hour == "1" ):
            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == "2"):
            hour_2 = 1
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == "3"):

            hour_2 = 0
            hour_3 = 1
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == "4"):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 1
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == "5"):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 1
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == "6"):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 1
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == "7"):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 1
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0   

        elif(hour == "8"):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 1
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0                   

        elif(hour == "9"):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 1
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == "10"):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 1
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == '11'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 1
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == '12'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 1
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == '13'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 1
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == '14'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 1
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == '15'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 1
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == '16'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 1
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == '17'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 1
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == '18'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 1
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == '19'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 1
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == '20'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 1
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == '21'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 1
            hour_22 = 0
            hour_23 = 0
            hour_24 = 0

        elif(hour == '22'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 1
            hour_23 = 0
            hour_24 = 0

        elif(hour == '23'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 1
            hour_24 = 0

        elif(hour == '24'):

            hour_2 = 0
            hour_3 = 0
            hour_4 = 0
            hour_5 = 0
            hour_6 = 0
            hour_7 = 0
            hour_8 = 0
            hour_9 = 0
            hour_10 = 0
            hour_11 = 0
            hour_12 = 0
            hour_13 = 0
            hour_14 = 0
            hour_15 = 0
            hour_16 = 0
            hour_17 = 0
            hour_18 = 0
            hour_19 = 0
            hour_20 = 0
            hour_21 = 0
            hour_22 = 0
            hour_23 = 0
            hour_24 = 1

    #     list_columns = ['temp', 'humidity', 'season_2', 'season_3', 'season_4', 'month_2',
    #    'month_3', 'month_4', 'month_5', 'month_6', 'month_7', 'month_8',
    #    'month_9', 'month_10', 'month_11', 'month_12', 'hour_1', 'hour_2',
    #    'hour_3', 'hour_4', 'hour_5', 'hour_6', 'hour_7', 'hour_8', 'hour_9',
    #    'hour_10', 'hour_11', 'hour_12', 'hour_13', 'hour_14', 'hour_15',
    #    'hour_16', 'hour_17', 'hour_18', 'hour_19', 'hour_20', 'hour_21',
    #    'hour_22', 'hour_23', 'holiday_1', 'weekday_1', 'weekday_2',
    #    'weekday_3', 'weekday_4', 'weekday_5', 'weekday_6', 'workingday_1',
    #    'weather_2', 'weather_3', 'weather_4']
        
        prediction=model.predict([[
            temp,
            humidity,
            season_2,
            season_3,
            season_4,            
            holiday_1,
            weekday_1,
            weekday_2,
            weekday_3,
            weekday_4,
            weekday_5,
            weekday_6,
            month_2,
            month_3,
            month_4,
            month_5,
            month_6,
            month_7,
            month_8,
            month_9,
            month_10,
            month_11,
            month_12,
            workingday_1,
            weather_2,
            weather_3,
            weather_4,
            hour_2,
            hour_3,
            hour_4,
            hour_5,
            hour_6,
            hour_7,
            hour_8,
            hour_9,
            hour_10,
            hour_11,
            hour_12,
            hour_13,
            hour_14,
            hour_15,
            hour_16,
            hour_17,
            hour_18,
            hour_19,
            hour_20,
            hour_21,
            hour_22,
            hour_23,
            hour_24,

        ]])

        output=np.expm1(prediction)

        return render_template('home.html',prediction_text="Bike count for today would be . {}".format(output))


    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)