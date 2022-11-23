import requests

cities = ('Лондон', 'Аэропорт Шереметьево', 'Череповец')
config = {'n':'', 'T':'', 'q':'', 'M':'', 'lang': 'ru'}
url_template = 'https://wttr.in/{}'

for city in cities:
    url = url_template.format(city)
    response = requests.get(url, params=config)
    response.raise_for_status()
    print(response.text)