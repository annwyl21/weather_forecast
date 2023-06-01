from flask import render_template, request
from application import app
from application.rain import Rain, get_weather_data
from application.form import LocationForm

@app.route('/')
def index():
    return render_template('index.html', title='Line-dried Laundry')

@app.route('/<location>')
def detail(location):
    if location == 'london':
        weather_forecast = Rain(get_weather_data('london'))
        return render_template('detail.html', title='London Weather', location='London', weather_forecast=weather_forecast)
    elif location == 'inverness':
        weather_forecast = Rain(get_weather_data('inverness'))
        return render_template('detail.html', title='Inverness Weather', location='Inverness', weather_forecast=weather_forecast)
