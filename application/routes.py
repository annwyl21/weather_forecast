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
        
        if form.location.data == 'london':
            weather_forecast = Rain(get_weather_data())
            
        elif form.location.data == 'oxford':
            weather_forecast = Rain(get_weather_data())
            
        elif form.location.data == 'cambridge':
            weather_forecast = Rain(get_weather_data())
            
        else:
            error_message = 'An error has occurred. Please try again.'
        
        return render_template('detail.html', title='Weather Details', weather_forecast=weather_forecast)

    return render_template('index.html', title='Line-dried Laundry', form=form, error_message=error_message)
