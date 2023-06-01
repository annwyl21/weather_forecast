from flask import render_template, request
from application import app
from application.rain import Rain, get_weather_data
from application.form import LocationForm

@app.route('/')
def index():
    return render_template('index.html', title='Line-dried Laundry')

@app.route('/detail')
def detail():
    weather_forecast = Rain(get_weather_data('london'))
    return render_template('detail.html', title='London Weather')
