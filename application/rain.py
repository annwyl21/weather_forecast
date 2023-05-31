import http.client
import os
import json

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
        self.today_temp = 0
        self.today_max_temp = 0
        self.today_min_temp = 0
        self.today_rain_prob = 0
        # self.tomorrow_temp = 0
        # self.tomorrow_max_temp = 0
        # self.tomorrow_min_temp = 0
        # self.tomorrow_rain_prob = 0
        # self.overmorrow_temp = 0
        # self.overmorrow_max_temp = 0
        # self.overmorrow_min_temp = 0
        # self.overmorrow_rain_prob = 0

    def set_weather(self):
        conn.request("GET", '/v0/forecasts/point/daily?latitude=51.5073&longitude=0.1657&Metadata=true', headers=headers)
        # Hyde Park, London 51.5073° N, 0.1657° W
        res = conn.getresponse()
        data = res.read()
        data_string = data.decode("utf-8")
        json_data = json.loads(data_string)

        weather_yesterday = json_data['features'][0]['properties']['timeSeries'][0]
        weather_today = json_data['features'][0]['properties']['timeSeries'][1]
        weather_tomorrow = json_data['features'][0]['properties']['timeSeries'][2]
        weather_overmorrow = json_data['features'][0]['properties']['timeSeries'][3]

        self.set_today_temp(weather_today)
        self.set_today_max_temp(weather_today)
        self.set_today_min_temp(weather_today)
        self.set_today_rain_prob(weather_today)

        # trying to create a forecast object with all the retrieved data

    def set_today_temp(self, weather_today):
        self.today_temp = int(weather_today['dayMaxScreenTemperature'])

    def set_today_max_temp(self, weather_today):
        self.today_max_temp = int(weather_today['dayUpperBoundMaxTemp'])

    def set_today_min_temp(self, weather_today):
        self.today_min_temp = int(weather_today['dayLowerBoundMaxTemp'])

    def set_today_rain_prob(self, weather_today):
        self.today_rain_prob = int(weather_today['nightProbabilityOfPrecipitation'])


        # self.tomorrow_temp = int(json_data['features'][0]['properties']['timeSeries'][2]['dayMaxScreenTemperature'])
        # self.tomorrow_max_temp = int(json_data['features'][0]['properties']['timeSeries'][2]['dayUpperBoundMaxTemp'])
        # self.tomorrow_min_temp = int(json_data['features'][0]['properties']['timeSeries'][2]['dayLowerBoundMaxTemp'])
        # self.tomorrow_rain_prob = int(json_data['features'][0]['properties']['timeSeries'][2]['nightProbabilityOfPrecipitation'])

        # self.overmorrow_temp = int(json_data['features'][0]['properties']['timeSeries'][3]['dayMaxScreenTemperature'])
        # self.overmorrow_max_temp = int(json_data['features'][0]['properties']['timeSeries'][3]['dayUpperBoundMaxTemp'])
        # self.overmorrow_min_temp = int(json_data['features'][0]['properties']['timeSeries'][3]['dayLowerBoundMaxTemp'])
        # self.overmorrow_rain_prob = int(json_data['features'][0]['properties']['timeSeries'][3]['nightProbabilityOfPrecipitation'])

    def get_today_temp(self):
            return self.today_temp
    
    def get_today_max_temp(self):
            return self.today_max_temp
    
    def get_today_min_temp(self):
            return self.today_min_temp
    
    def get_today_rain_prob(self):
            return self.today_rain_prob

if __name__ == "__main__":
    Rain.set_weather('London')

