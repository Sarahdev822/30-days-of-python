#Exercises: Level 1
#Write a function which generates a six digit/character random_user_id
import random
import string
def random_user_id():
  characters = string.ascii_letters + string.digits
  return ''.join(random.choices(characters, k=6))

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
  num_chars = int(input("Enter the number of characters per ID: "))
  num_ids = int(input("Enter the number of IDs to generate: "))
  characters = string.ascii_letters + string.digits
  for _ in range(num_ids):
    new_id = ''.join(random.choices(characters, k=num_chars))
    print(new_id)

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
from random import randint
def rgb_color_gen():
  color1 = randint(0, 255)
  color2 = randint(0, 255)
  color3 = randint(0, 255)
  print(f'rgb({color1}, {color2}, {color3})')

#Exercises: Level 2
#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors():
  alpha_num = "0123456789abcdef"
  color = '#'
  for _ in range(7):
    color += random.choice(alpha_num)
  return color

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num):
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  f'rgb({r}, {g}, {b})'
  colors = []
  for _ in range(num):
    colors.append(f'rgb({r}, {g}, {b})')
  return colors

#Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color,num):
  results = []
  if(color == 'hexa'):
    for _ in range(num):
      hexa_color = list_of_hexa_colors()
      results.append(hexa_color)
    return results  
  elif color == 'rgb':
    rgb_color = list_of_rgb_colors(num)
    return rgb_color

#Exercises: Level 3
#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(list):
  list_copy = list.copy()
  random.shuffle(list_copy)
  return list_copy

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def random_numbers():
  return random.sample(range(0,  10), 7)

print(random_numbers())