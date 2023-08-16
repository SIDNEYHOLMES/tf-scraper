import requests
from bs4 import BeautifulSoup

request_results = requests.get('https://wiki.teamfortress.com/wiki/Weapons')
wiki_page = BeautifulSoup(request_results.text, "html.parser")

# Find all the tables with class 'wikitable grid'
all_tables = wiki_page.find_all('table', class_='wikitable grid')

# Create a list to store weapon objects
weapon_objects = []

# Loop through each table and find the <a> tags with title data
for table in all_tables:
    rows = table.find_all('tr')
    for row in rows:
        th_tag = row.find('th')
        if th_tag:
            a_tag = th_tag.find('a', title=True)
            if a_tag:
                title_data = a_tag['title']
                
                # Find the text of the <small> tag containing the weapon type
                small_tag = th_tag.find('small')
                weapon_type = small_tag.get_text() if small_tag else 'unknown'  # Default to 'unknown' if small tag not found
                
                # Find the <img> tag inside the <a> tag and extract the 'src' 
                img_tag = a_tag.find('img')
                image_src = img_tag['src'] if img_tag else ''
                
                # and create the weapon object dictionary
                weapon_object = {
                    'name': title_data,
                    'class': '',  # needs manual input (could be array or string)
                    'type': weapon_type,
                    'image': image_src
                }
                
                # Append the weapon object to the list
                weapon_objects.append(weapon_object)

# Print the weapon objects list
for weapon in weapon_objects:
    print(weapon)
