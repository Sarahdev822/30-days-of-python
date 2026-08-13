#Read this url and find the 10 most frequent words.
import requests
import re
from collections import Counter
import statistics
romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
def ten_words_from_url(url):
  response = requests.get(url)
  text = response.text
  words = re.findall(r'\w+', text.lower())
  word_counts = Counter(words)
  return word_counts.most_common(10)

print(ten_words_from_url(romeo_and_juliet))

#Read the cats API and
#find the min, max, mean, median, standard deviation of cats' weight in metric units.
#the min, max, mean, median, standard deviation of cats' lifespan in years.
#Create a frequency table of country and breed of cats
import requests
import statistics
from collections import Counter

cats_api = 'https://api.thecatapi.com/v1/breeds'

def parse_range(range_str):
    parts = [float(x.strip()) for x in range_str.split('-')]
    return sum(parts) / len(parts)

def get_stats(data_list):
    return {
        "Min": round(min(data_list), 2),
        "Max": round(max(data_list), 2),
        "Mean": round(statistics.mean(data_list), 2),
        "Median": round(statistics.median(data_list), 2),
        "Std Dev": round(statistics.stdev(data_list), 2)
    }

def analyze_cat_data(url):
    response = requests.get(url)
    data = response.json()
    
    weights = []
    lifespans = []
    country_breed_pairs = []
    
    for cat in data:
        if 'weight' in cat and 'metric' in cat['weight']:
            weights.append(parse_range(cat['weight']['metric']))
        if 'life_span' in cat:
            lifespans.append(parse_range(cat['life_span']))
        country = cat.get('origin', 'Unknown')
        breed = cat.get('name', 'Unknown')
        country_breed_pairs.append((country, breed))

    weight_stats = get_stats(weights)
    lifespan_stats = get_stats(lifespans)
    country_counts = Counter(country for country, breed in country_breed_pairs)

    print("=== Weight Statistics (Metric Units: kg) ===")
    for stat, val in weight_stats.items():
        print(f"{stat}: {val}")

    print("\n=== Lifespan Statistics (Years) ===")
    for stat, val in lifespan_stats.items():
        print(f"{stat}: {val}")

    print("\n=== Frequency Table: Country vs Number of Breeds ===")
    print(f"{'Country':<25} | {'Breed Count':<10}")
    print("-" * 40)
    for country, count in country_counts.most_common():
        print(f"{country:<25} | {count:<10}")


#Read the countries API and find
#i the 10 largest countries
#ii the 10 most spoken languages
#iii the total number of languages in the countries API
