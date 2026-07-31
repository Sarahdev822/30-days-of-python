#Exercises: Level 1
# Define a call function before map, filter or reduce, see examples.
from functools import reduce
def cubed(num):
  return num ** 3
def even(num):
  return num % 2 == 0
def sum(num,next_num):
  return num + next_num

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Use for loop to print each country in the countries list.
for country in countries:
  print(country)

#Use for to print each name in the names list.
for name in names:
  print(name)

#Use for to print each number in the numbers list.
for num in numbers:
  print(num)

#Exercises: Level 2
#Use map to create a new list by changing each country to uppercase in the countries list
def upper_case(country):
  return country.upper()
country_to_upper = map(upper_case, countries)
print(list(country_to_upper))

#Use map to create a new list by changing each number to its square in the numbers list
def square(num):
  return num ** 2
squared_numbers = map(square, numbers)
print(list(squared_numbers))

#Use map to change each name to uppercase in the names list
def name_upper(name):
  return name.upper()
upper_names = map(name_upper, names)
print(list(upper_names))

#Use filter to filter out countries containing 'land'.
def nonland_countries(country):
  return "land" not in country.lower()
nonland = filter(nonland_countries, countries)
print(list(nonland))

#Use filter to filter out countries starting with an 'E'
def ee_countries(country):
  return country[0] == "E"
e_countries = filter(ee_countries, countries)
print(list(e_countries))

#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
stacked = reduce(sum, map(cubed, filter(even, numbers)))
print(stacked)

#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
  results = []
  for item in lst:
    if(type(item) == str):
      results.append(item)
  return results

#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def join_sentence(country,nextcountry):
  if nextcountry == countries[-1]:
    return country + " and " + nextcountry
  else:
   return country + ", " + nextcountry 
sentence = reduce(join_sentence, countries)
final_countries = " are north European countries"
complete_sentence = sentence + final_countries
print(complete_sentence)

#Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
def categorize_countries(pattern):
  results = []
  for country in countries:
    if pattern in country:
      results.append(country)
  return results

#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
from collections import Counter

def country_dictionary():
  return dict(Counter(country[0] for country in countries))

#Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries():
  return countries[:10]

#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_countries():
  return countries[-11:-1]
