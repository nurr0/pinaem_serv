import requests
import time
import datetime

url = 'https://atoma-horoscope.onrender.com/horoscope/cancer/full/'

sleep_time = 60

while True:
    Response = requests.get(url)
    if Response.status_code == 200:
        print(f'[{datetime.datetime.now()}] - |{Response.status_code}| Ответ от сервера успешно получен')
    else:
        print(f'[{datetime.datetime.now()}] - |{Response.status_code}| Сервер ответил с ошибкой(не 200)')
    time.sleep(sleep_time)
