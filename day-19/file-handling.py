#Exercies: Level 1
#Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
def count_lines_and_words(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        lines_count = len(lines)
        words_count = sum(len(line.split()) for line in lines)
    return lines_count, words_count

obama_speech = open("./day-19/obama_speech.txt", "r")
lines = obama_speech.readlines()
lines_count = len(lines)
words_count = sum(len(line.split()) for line in lines)
print(lines_count)
print(words_count)
obama_speech.close()

#Read michelle_obama_speech.txt file and count number of lines and words
michelle_obama_speech = open("./day-19/michelle_obama_speech.txt", "r")
lines = michelle_obama_speech.readlines()
lines_count = len(lines)
word_count = sum(len(line.split()) for line in lines)
print(lines_count)
print(word_count)
michelle_obama_speech.close()

#Read donald_speech.txt file and count number of lines and words
donald_speech = open("./day-19/donald_speech.txt", "r")
lines = donald_speech.readlines()
lines_count = len(lines)
word_count = sum(len(line.split()) for line in lines)
print(lines_count)
print(word_count)
donald_speech.close()

#Read melina_trump_speech.txt file and count number of lines and words
melina_trump_speech = open("./day-19/melina_trump_speech.txt", "r")
lines = melina_trump_speech.readlines()
lines_count = len(lines)
word_count = sum(len(line.split()) for line in lines)
print(lines_count)
print(word_count)
melina_trump_speech.close()


#Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json
def most_spoken_languages(file_path, top_n=10):
  with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
  language_count = {}
  for country in data:
    for language in country.get("languages", []):
      language_count[language] = language_count.get(language, 0) + 1
  sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
  result = [(count, lang) for lang, count in sorted_languages[:top_n]]
  return result

print(most_spoken_languages('./day-19/data_countries.json'))

#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries(file_path, top_n=10):
  with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
  sorted_countries = sorted(data, key=lambda x: x.get("population", 0), reverse=True)
  result = [{'country': country.get("name"), 'population': country.get("population")} for country in sorted_countries[:top_n]]
  return result

print(most_populated_countries('./day-19/data_countries.json'))


#Exercises: Level 2
#Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
with open('./day-19/email_exchange_big.txt', 'r', encoding='utf-8') as file:
   content = file.read()
unique_emails = set(re.findall(email_pattern, content))


#Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
def find_most_common_words(strfile, n):
  if isinstance(strfile, str):
    with open(strfile, 'r', encoding='utf-8') as file:
      content = file.read()
  else:
    content = strfile

  words = content.lower().split()
  word_count = {}
  for word in words:
    word_count[word] = word_count.get(word, 0) + 1

  sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
  return sorted_words[:n]

#Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
import re
import os
from stop_words import stop_words
def clean_text(text):
  text = text.lower()  
  clean_str = re.sub(r'[^\w\s]', ' ', text)
  words = clean_str.split()
  return words

def remove_support_words(words): 
  filtered_words = [word for word in words if word not in stop_words]
  return filtered_words   

def check_text_similarity(text1, text2, stop_words):
  words1 = clean_text(text1)
  words2 = clean_text(text2)
  filtered_words1 = remove_support_words(words1, stop_words)
  filtered_words2 = remove_support_words(words2, stop_words)
  set1 = set(filtered_words1)
  set2 = set(filtered_words2)
  common_words = set1.intersection(set2)
  total_unique_words = len(set1.union(set2))
  similarity_percentage = (len(common_words) / total_unique_words) * 100 if total_unique_words > 0 else 0
  return round(similarity_percentage, 2)
   
#Find the 10 most repeated words in the romeo_and_juliet.txt
def find_most_repeated_words(file_path, n):
  with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
  words = content.lower().split()
  word_count = {}
  for word in words:
    word_count[word] = word_count.get(word, 0) + 1
  sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
  return sorted_words[:n]

#Read the hacker news csv file and find out:
#i.Count the number of lines containing python or Python
hacker_news_file = './day-19/hacker_news.csv'
with open(hacker_news_file, 'r', encoding='utf-8') as file:
  lines = file.readlines()
  python_lines_count = sum(1 for line in lines if 'python' in line.lower())
print(f"Number of lines containing 'python' or 'Python': {python_lines_count}")

#ii.Count the number lines containing JavaScript, javascript or Javascript
javascript_lines_count = sum(1 for line in lines if 'javascript' in line.lower())
print(f"Number of lines containing 'JavaScript', 'javascript' or 'Javascript': {javascript_lines_count}")

#iii.Count the number lines containing Java and not JavaScript
java_lines_count = sum(1 for line in lines if 'java' in line.lower() and 'javascript' not in line.lower())
print(f"Number of lines containing 'Java' and not 'JavaScript': {java_lines_count}")