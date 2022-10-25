import requests
from datetime import datetime


city_name = input('Enter the name of city to view its temperature\n')
api_key = '97788340cd382a88c46c12b1c3d95762'
full_link = 'https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid='+api_key


api_link = requests.get(full_link)
api_data = api_link.json()

date_time = datetime.now().strftime('%d %b %Y | %I:%M:%S %p')
city_temp = ((api_data['main']['temp'])-273.5)
city_humidity = (api_data['main']['humidity'])
max_temp = ((api_data['main']['temp_max'])-273.5)
min_temp = ((api_data['main']['temp_min'])-273.5)
weather_description = (api_data['weather'][0]['description'])
wind_speed = (api_data['wind']['speed'])

print('-----------------------------------------------------------------------------------------------\n')
print('Weather details : {} || {}'.format(city_name, date_time))
print()
print("Temperature         : {:.2f} degree c".format(city_temp))
print("Weather Description :", weather_description)
print("Wind speed          :", wind_speed, "kmph")
print("Humidity            :", city_humidity)
print("Maximum temperature : {:.2f} degree c".format(max_temp))
print("Minimum Temperature : {:.2f} degree c".format(min_temp))


