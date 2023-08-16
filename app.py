import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

request_results = requests.get('https://wiki.teamfortress.com/wiki/Weapons')
wiki_page = BeautifulSoup(request_results.text, "html.parser")

# Find all the tables with class 'wikitable grid'
all_tables = wiki_page.find_all('table', class_='wikitable grid')

# store unique title data in order
unique_titles = OrderedDict()

# Loop through each table and find the <a> tags with title data
for table in all_tables:
    wiki_links = table.find_all('a', title=True)
    for a_tag in wiki_links:
        title_data = a_tag['title']
        unique_titles[title_data] = None

# Print the unique title data in the order they were encountered
for title in unique_titles.keys():
    print(title)
