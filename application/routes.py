from flask import render_template
from application import app
from application.rain import Rain

@app.route('/')
def index():
    rain = Rain(20)
    rain_risk = 'low'
    return render_template('index.html', title='Line-dried Laundry', rain=rain, rain_risk=rain_risk)

