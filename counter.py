import json
import urllib.request
class WeatherText(object):
    def toarr(self):
        apiKey = "68omtQAk71JeqLo3TdwwVg1awlyVS5UL"
        results = 50  # 50,100,150
        contents = urllib.request.urlopen(
            "http://dataservice.accuweather.com/currentconditions/v1/topcities/" + str(
                results) + "?apikey=" + apiKey).read()
        arr = json.loads(contents)
        return arr
    def get_key(self):
        weather_type=[]
        arr=self.toarr()
        for i in range(len(arr)):
            weather_type.append(arr[i]['WeatherText'])
        return weather_type
    def filter(self):
        return
obj=WeatherText()
print(obj.get_key())

