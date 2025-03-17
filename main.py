import requests

from config import TOKEN

base_url = F'https://api.telegram.org/bot{TOKEN}/'
command = 'getMe'

response = requests.get(base_url + command)

print(response .json())

