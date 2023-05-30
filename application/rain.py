import http.client

conn = http.client.HTTPSConnection("api-metoffice.apiconnect.ibmcloud.com")

headers = {
    'X-IBM-Client-Id': "clientId",
    'X-IBM-Client-Secret': "clientSecret",
    'accept': "application/json"
    }

class Rain:
    def __init__(self, rain_forecast):
        self.rain_forecast = rain_forecast

    def get_rain_forecast(self):
        conn.request("GET", "/v0/forecasts/point/daily?excludeParameterMetadata=true&include&latitude=51.5073&longitude=0.1657", headers=headers)
        # Hyde Park, London 51.5073° N, 0.1657° W
        res = conn.getresponse()
        data = res.read()
        self.rain_forecast = data.decode("utf-8")
        return self.rain_forecast

    def set_rain_forecast(self, rain_forecast):
        self.rain_forecast = rain_forecast

    def __str__(self):
        return f"Rain forecast: {self.rain_forecast}"