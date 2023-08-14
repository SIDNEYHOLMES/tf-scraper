import requests
from bs4 import BeautifulSoup

request_results = requests.get('https://wiki.teamfortress.com/wiki/Weapons')

wiki_page = BeautifulSoup(request_results.text, "html.parser")

# print(wiki_page.prettify)
weapon_name = wiki_page

print(wiki_page.find('table', class_='wikitable grid'))