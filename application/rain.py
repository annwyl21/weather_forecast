import http.client
import os

conn = http.client.HTTPSConnection("api-metoffice.apiconnect.ibmcloud.com")
userid = os.environ.get('X-IBM-Client-Id')
key = os.environ.get('X-IBM-Client-Secret')

headers = {
    'X-IBM-Client-Id': userid,
    'X-IBM-Client-Secret': key,
    'accept': "application/json"
    }

class Rain:
    def __init__(self, location):
        self.location = 'location'

    def get_rain_forecast(self):
        conn.request("GET", '/v0/forecasts/point/daily?latitude=51.5073&longitude=0.1657&Metadata=true', headers=headers)
        # Hyde Park, London 51.5073° N, 0.1657° W
        res = conn.getresponse()
        data = res.read()
        data_string = data.decode("utf-8")
        weather_data = data_string.split(',')
        print(weather_data[0])

        # for feature in weather_data['features']:
        #     for time_series in feature['properties']['timeSeries']:
        #         temp = time_series['dayMaxScreenTemperature']
        #         max_temp = time_series['dayUpperBoundMaxTemp']
        #         min_temp = time_series['dayLowerBoundMaxTemp']
        #         rain_prob = time_series['nightProbabilityOfPrecipitation']
        #         print(temp, max_temp, min_temp, rain_prob)
         

    def set_rain_forecast(self, rain_forecast):
        self.rain_forecast = rain_forecast

    def __str__(self):
        return f"Rain forecast: {self.rain_forecast}"

if __name__ == "__main__":
    Rain.get_rain_forecast('London')

