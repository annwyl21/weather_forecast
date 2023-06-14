import http.client
import os
import json

# establish a connection and retrieve location specific weather data in a function
def get_weather_data(location):
    location = location.lower()
    locations_dict = {
        'london': [51.5073, 0.1657], 
        'inverness': [57.4778, 4.2247],
        }

    conn = http.client.HTTPSConnection("api-metoffice.apiconnect.ibmcloud.com")
    userid = os.environ.get('X-IBM-Client-Id')
    key = os.environ.get('X-IBM-Client-Secret')

    headers = {
    'X-IBM-Client-Id': userid,
    'X-IBM-Client-Secret': key,
    'accept': "application/json"
    }

    latitude = str(locations_dict[location][0])
    longitude = str(locations_dict[location][1])
    print('Identified location:', latitude, longitude)

    # conn.request("GET", '/v0/forecasts/point/daily?latitude=51.5073&longitude=0.1657&Metadata=true', headers=headers)
    conn.request("GET", '/v0/forecasts/point/daily?latitude=' + latitude + '&longitude=' + longitude + '&Metadata=true', headers=headers)
    # Hyde Park, London 51.5073° N, 0.1657° W
    print('request sent')
    res = conn.getresponse()
    data = res.read()
    data_string = data.decode("utf-8")
    
    json_data = json.loads(data_string)
    print('weather data retrieved')
    return json_data

# extract the data needed from the response and store as an object
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
        self.today_snow_prob = int(weather_today['nightProbabilityOfSnow'])

        weather_tomorrow = weather_data['features'][0]['properties']['timeSeries'][2]
        self.tomorrow_temp = int(weather_tomorrow['dayMaxScreenTemperature'])
        self.tomorrow_rain_prob = int(weather_tomorrow['nightProbabilityOfPrecipitation'])

        weather_overmorrow = weather_data['features'][0]['properties']['timeSeries'][3]
        self.overmorrow_temp = int(weather_overmorrow['dayMaxScreenTemperature'])
        self.overmorrow_rain_prob = int(weather_overmorrow['nightProbabilityOfPrecipitation'])

        if self.yesterday_rain_prob < 25 and self.today_rain_prob < 25 and self.tomorrow_rain_prob < 25 and self.overmorrow_rain_prob < 25:
            self.dry_spell = True
        
        if self.today_rain_prob >25:
            self.rainy_day = True

        if self.today_temp > 25:
            self.hot_day = True
        elif self.today_temp < 10 and self.today_temp > 4:
            self.cold_day = True
        elif self.today_temp < 4:
            self.freezing_day = True

        if self.today_snow_prob > 85:
            self.snowy_day = True
    
    #def convert_to_fahrenheit(self, celsius):
    #    return int(celsius * 9/5 + 32)


if __name__ == "__main__":
    myrain = Rain(get_weather_data(location='london'))
    print(myrain)
