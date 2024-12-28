"""
Это погодное приложение, которое работает на Python библиотеке requests, plyer.
pip install plyer requests pyinstaller

Образец ссылки url = 'https://api.openweathermap.org/data/2.5/weather?q=Москва&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru' 

Образец ссылки https://api.openweathermap.org/data/2.5/weather?q=Москва&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru

{'coord': {'lon': 37.6156, 'lat': 55.7522}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'облачно с прояснениями', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 0.93, 'feels_like': -3.44, 'temp_min': 0.24, 'temp_max': 0.93, 'pressure': 1022, 'humidity': 61, 'sea_level': 1022, 'grnd_level': 1002}, 'visibility': 10000, 'wind': {'speed': 4.47, 'deg': 214, 'gust': 11.97}, 'clouds': {'all': 64}, 'dt': 1733247335, 'sys': {'type': 2, 'id': 2095214, 'country': 'RU', 'sunrise': 1733204316, 'sunset': 1733230838}, 'timezone': 10800, 'id': 524901, 'name': 'Москва', 'cod': 200}
"""

from urllib import response
import requests
from plyer import notification

API_KEY = r'89d4ef259b167357f183cf4ab0d66ff3'
CITY = 'Пенза'


def get_weather(city: str, api_key: str) -> dict:
    """
    Функция, котрая делает запрос к погодному API и возвращает данные о погоде в виде словаря
    """
    url = fr'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    response = requests.get(url)
    return response.json()


def format_weather_message(weather_dict:dict) -> str:
    """
    Функция, которая принимает словарь с данными о погоде и возвращает строку с сообщением
    """
    temp = weather_dict['main']['temp'] # температура
    feels_like = weather_dict['main']['feels_like'] # ощущается как
    description = weather_dict['weather'][0]['description'] # описание
    return f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}'
    
     
def notify_weather(message:str) -> None:
    """
    Функция, которая отправляет уведомления с погодой
    """
    notification.notify(
    title = f'Погода в {CITY}',
    message=message,
    app_name = 'My Weather App',
    app_icon=None)

def main():
    """
    Функция, которая запускает приложение и запускает все остальные функции
    """
    weather_dict = get_weather(CITY, API_KEY)
    message = format_weather_message(weather_dict)
    notify_weather(message)

main()