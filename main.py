import requests
from bs4 import BeautifulSoup

url = 'https://shopee.co.id/'
# try:
#      r = requests.get(url)
#      if r.status_code == 200:
#          print(f'Sukses ! status code {r}')
#          print('Content ',r.text)
#      else:
#          print(f'gak nemu !{r.status_code}')
#
# except Exception as e:
#      print(e)