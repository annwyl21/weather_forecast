class Rain:
    def __init__(self, rain_forecast):
        self.rain_forecast = rain_forecast

    def get_rain_forecast(self):
        return self.rain_forecast

    def set_rain_forecast(self, rain_forecast):
        self.rain_forecast = rain_forecast

    def __str__(self):
        return f"Rain forecast: {self.rain_forecast}"