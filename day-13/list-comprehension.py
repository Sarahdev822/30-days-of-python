#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_and_zero = [i for i in numbers if i <= 0]

#Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
single_list = [number for row in list_of_lists for number in row]

#Using list comprehension create the following list of tuples:
powers = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]

#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_countries = [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist]

#Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_dict = [{'country':country, 'city':city} for sublist in countries for country, city in sublist]

#Change the following list of lists to a list of concatenated strings:
list_of_list = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
list_of_strings = [f'{first_name} {last_name}' for list in list_of_list for first_name, last_name in list]

#Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, x2, y1, y2: (x2 - x1) / (y2 - y1)
print(slope(2,5,4,10))