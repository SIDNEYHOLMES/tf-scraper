import requests
from bs4 import BeautifulSoup

request_results = requests.get('https://wiki.teamfortress.com/wiki/Weapons')
wiki_page = BeautifulSoup(request_results.text, "html.parser").find('table', class_='wikitable grid').find_all('a', title=True)

print(wiki_page)

for a_tag in wiki_page:
    title_data = a_tag['title']
    print(title_data)
