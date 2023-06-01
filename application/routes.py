from flask import render_template, request
from application import app
from application.rain import Rain, get_weather_data
from application.form import LocationForm

@app.route('/')
def index():
    error_message = ''
    form = LocationForm()
    if request.method == 'POST':
        location = form.location.data
        if not location:
            error_message = 'Please select a location.'
        else:
            weather_forecast = Rain(get_weather_data(location))
            return render_template('detail.html', title='Weather Details', weather_forecast=weather_forecast)

    return render_template('index.html', title='Line-dried Laundry', form=form, error_message=error_message)
