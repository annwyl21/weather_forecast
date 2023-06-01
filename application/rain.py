import http.client
import os
import json



def get_weather_data():
    conn = http.client.HTTPSConnection("api-metoffice.apiconnect.ibmcloud.com")
    userid = os.environ.get('X-IBM-Client-Id')
    key = os.environ.get('X-IBM-Client-Secret')

    headers = {
    'X-IBM-Client-Id': userid,
    'X-IBM-Client-Secret': key,
    'accept': "application/json"
    }

    conn.request("GET", '/v0/forecasts/point/daily?latitude=51.5073&longitude=0.1657&Metadata=true', headers=headers)
    # Hyde Park, London 51.5073° N, 0.1657° W
    res = conn.getresponse()
    data = res.read()
    data_string = data.decode("utf-8")
    json_data = json.loads(data_string)
    return json_data

class Rain:
    def __init__(self, weather_data):

        weather_yesterday = weather_data['features'][0]['properties']['timeSeries'][0]
        self.yesterday_temp = int(weather_yesterday['dayMaxScreenTemperature'])
        self.yesterday_max_temp = int(weather_yesterday['dayUpperBoundMaxTemp'])
        self.yesterday_min_temp = int(weather_yesterday['dayLowerBoundMaxTemp'])
        self.yesterday_rain_prob = int(weather_yesterday['nightProbabilityOfPrecipitation'])

        weather_today = weather_data['features'][0]['properties']['timeSeries'][1]
        self.today_temp = int(weather_today['dayMaxScreenTemperature'])
        self.today_max_temp = int(weather_today['dayUpperBoundMaxTemp'])
        self.today_min_temp = int(weather_today['dayLowerBoundMaxTemp'])
        self.today_rain_prob = int(weather_today['nightProbabilityOfPrecipitation'])

        weather_tomorrow = weather_data['features'][0]['properties']['timeSeries'][2]
        self.tomorrow_temp = int(weather_tomorrow['dayMaxScreenTemperature'])
        self.tomorrow_rain_prob = int(weather_tomorrow['nightProbabilityOfPrecipitation'])

        weather_overmorrow = weather_data['features'][0]['properties']['timeSeries'][3]
        self.overmorrow_temp = int(weather_overmorrow['dayMaxScreenTemperature'])
        self.overmorrow_rain_prob = int(weather_overmorrow['nightProbabilityOfPrecipitation'])

    def get_yesterday_temp(self):
        return self.yesterday_temp
    
    def get_yesterday_max_temp(self):
        return self.yesterday_max_temp
    
    def get_yesterday_min_temp(self):
        return self.yesterday_min_temp
    
    def get_yesterday_rain_prob(self):
        return self.yesterday_rain_prob
    
    def get_today_temp(self):
        return self.today_temp
    
    def get_today_max_temp(self):
        return self.today_max_temp
    
    def get_today_min_temp(self):
        return self.today_min_temp
    
    def get_today_rain_prob(self):
        return self.today_rain_prob
    
    def get_tomorrow_temp(self):
        return self.tomorrow_temp
    
    def get_tomorrow_rain_prob(self):
        return self.tomorrow_rain_prob
    
    def get_overmorrow_temp(self):
        return self.overmorrow_temp
    
    def get_overmorrow_rain_prob(self):
        return self.overmorrow_rain_prob



if __name__ == "__main__":
    myrain = Rain(get_weather_data())
