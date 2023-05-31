from flask import render_template
from application import app
from application.rain import Rain

@app.route('/')
def index():
    forecast_instance = Rain.set_weather('London')
    rain_probability = forecast_instance.get_today_rain_prob()
    if rain_probability <= 25:
        rain_risk = 'low'
    elif rain_probability >= 50:
        rain_risk = 'high'
    else:
        rain_risk = 'medium'
    return render_template('index.html', title='Line-dried Laundry', today=forecast_instance, rain_risk = rain_risk)

@app.route('/detail')
def details():
    return render_template('detail.html', title='Weather Details')