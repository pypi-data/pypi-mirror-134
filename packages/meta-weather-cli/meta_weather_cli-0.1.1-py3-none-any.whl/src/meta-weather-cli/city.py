import requests
import datetime
import calendar
import fire

def get_world_id(city):
    url = f"https://www.metaweather.com/api/location/search/?query={city}"
    response = requests.get(url)
    city_stats = response.json()
    if not city_stats:
        raise fire.core.FireError("No such city in the metaweather API.")
    elif len(city_stats) > 1:
        raise fire.core.FireError("You probably didn't finish the name of the city.")
    return city_stats[0]["woeid"]

def get_temperature(world_id):
    url = f"https://www.metaweather.com/api/location/{world_id}/"
    response = requests.get(url)
    weather_stats = response.json()
    temperatures = [round(int(day["the_temp"])) for day in weather_stats["consolidated_weather"]]
    weekday = datetime.date.today().weekday()
    weekdays = list(calendar.day_name)
    days = ["Today", "Tomorrow"]
    days += weekdays[(weekday + 2) % 6 : (weekday + 5) % 6]
    return dict(zip(days, temperatures))
