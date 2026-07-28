#Exercises Level 1
def add_two_numbers(a, b):
    return a + b

def area_of_a_circle(radius):
    area = float(3.14 * radius ** 2)
    return area

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums (*args):
    sum = 0
    for num in args:
        if isinstance(num, (int, float)):
            sum += num
        else:
            return "All arguments must be numbers."
    return sum

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def conert_celcius_to_fahrenheit(cels):
    faren = (cels * 9/5) + 32
    return faren

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    else:
        return 'Summer'

#Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)."
    slope = (y2 - y1) / (x2 - x1)
    return slope

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import cmath
def solve_quadratic_eqn(a, b, c):
    discrimant = b**2 - 4*a*c
    soln1 = (-b + cmath.sqrt(discrimant)) / (2*a)
    soln2 = (-b - cmath.sqrt(discrimant)) / (2*a)
    return soln1, soln2

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list (lists):
    for item in lists:
        print (item)

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    results = []
    for items in range(len(array) - 1, -1, -1):
        results.append(array[items])
    return results

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list):
    capitalized_list = []
    for items in list:
        capitalized_list.append(items.upper())
    return capitalized_list

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_iems(list,item):
    list.append(item)
    return list

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(list2, item2):
    list2.pop(item2)
    return list2

#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(nums):
    sum = 0
    for num in range(nums + 1):
        sum += num
    return sum

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds (nums):
    sum = 0
    for num in range(nums + 1):
        if(num % 2 != 0):
            sum += num
    return sum

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(number):
    sum = 0
    for num in range(number + 1):
        if(num % 2 == 0):
            sum += num
    return sum


#Exercises: Level 2
#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(interger):
    evens = 0
    odds =0
    for num in range(interger + 1):
        if(num % 2 == 0):
            evens += 1
        elif(num % 2 != 0):
            odds += 1
    print(f'The number of evens are {evens}.')
    print(f'The number of odds are {odds}.')

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    factorial = 1
    for num in range(1, number + 1):
        factorial *= num
    return factorial

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(para):
    return not para

#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lists):
    total = 0
    for i in lists:
        total += i
    mean = int(total) / int(len(lists))
    return mean

def calculate_median(lists):
    sorted_lists = sorted(lists)
    n = len(lists)
    middle_index = n // 2
    if(n % 2 == 0):
        left_num = sorted_lists[middle_index -1]
        right_num = sorted_lists[middle_index]
        return int(right_num + left_num) /2
    else:
        return sorted_lists[middle_index]

def calculate_mode(lists):
    counts = {}
    for item in lists:
        counts[item] = counts.get(item, 0) + 1
    max_count = max(counts.values())
    modes = [item for item, count in counts.items() if count == max_count]
    return modes

def calculate_range(lists):
    sorted_list = sorted(lists)
    smallest = sorted_list[0]
    largest = sorted_list[int(len(sorted_list)) - 1]
    range = largest - smallest
    return range

def calculate_variance(lists):
    mean = calculate_mean(lists)
    sum_of_squared = 0
    for num in lists:
        sum_of_squared += (mean - num) ** 2
    return sum_of_squared / len(lists)

import math
def calculate_std(lists):
    variance = calculate_variance(lists)
    return math.sqrt(variance)

#Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
def greet(name = 'Guest'):
    print(f'Hello, {name}!')

#Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
