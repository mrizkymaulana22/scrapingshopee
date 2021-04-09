import requests
from bs4 import BeautifulSoup

url = 'https://remoteworker.id/'

req = requests.get(url)

html_parse = BeautifulSoup(req.text, "html.parser")

data = html_parse.find('h1', class_='s_title_default')
print(data)
