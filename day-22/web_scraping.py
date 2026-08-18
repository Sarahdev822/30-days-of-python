#Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').

import requests
from bs4 import BeautifulSoup
import json
import re

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

def scrape_bu_facts(target_url):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
  }
  response = requests.get(target_url, headers=headers)
  if response != 200:
    print(f"Failed to fetch page. Status code: {response.status_code}")
    return
  soup = BeautifulSoup(response.text, 'html.parser')
  scraped_data = []
  sections = soup.find_all(['section', 'div'], class_=re.compile(r'fact|stat|content', re.I))
  for header in soup.find_all(['h2', 'h3']):
    category_name = header.get_text(strip=True)
    facts = []
    next_elem = header.find_next_sibling()
    while next_elem and next_elem.name not in ['h2', 'h3']:
      if next_elem.name == 'ul':
       facts.extend([li.get_text(strip=True) for li in next_elem.find_all('li')])
      elif next_elem.name == 'p':
        text = next_elem.get_text(strip=True)
        if text:
          facts.append(text)
      next_elem = next_elem.find_next_sibling()

    if facts:
      scraped_data.append({
        "category": category_name,
        "facts": facts
      })

  output_filename = "bu_facts.json"
  with open(output_filename, "w", encoding="utf-8") as json_file:
    json.dump(scraped_data, json_file, indent=4, ensure_ascii=False)
  print(f"Successfully scraped data and saved to {output_filename}!")


scrape_bu_facts(url)