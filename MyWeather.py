Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... import json
... 
... def get_weather(city):
...     api_key = "784c0c573426c0715bada8aafd4cd39b"  # Вставьте сюда ваш API ключ OpenWeatherMap
...     base_url = "http://api.openweathermap.org/data/2.5/weather"
...     params = {
...         "q": city,
...         "appid": api_key,
...         "units": "metric"
...     }
...     response = requests.get(base_url, params=params)
...     weather_data = json.loads(response.text)
...     return weather_data
... 
... def display_weather(weather_data):
...     if weather_data["cod"] != "404":
...         main_data = weather_data["main"]
...         weather = weather_data["weather"][0]
...         print(f"Температура: {main_data['temp']}°C")
...         print(f"Ощущается как: {main_data['feels_like']}°C")
...         print(f"Погодные условия: {weather['description']}")
...     else:
...         print("Город не найден.")
... 
... def main():
...     city = input("Shyolkovo: ")
...     weather_data = get_weather(city)
...     display_weather(weather_data)
... 
... if __name__ == "__main__":
...     main()
