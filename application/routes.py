from flask import render_template, request
from application import app
from application.rain import Rain, get_weather_data
from application.form import LocationForm

@app.route('/')
def index():
    return render_template('index.html', title='Line-dried Laundry')

@app.route('/location/<location>')
def detail(location):
    if location == 'inverness':
        weather_forecast = Rain(get_weather_data('inverness'))
        pagetitle='Inverness Weather'
    else:
        location == 'london'
        weather_forecast = Rain(get_weather_data('london'))
        pagetitle='London Weather'
    return render_template('detail.html', title=pagetitle, location=location, weather_forecast=weather_forecast)
