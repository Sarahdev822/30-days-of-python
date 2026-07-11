#Exercises: Level 1
empty_tuple = ()
brothers = ('Dawg','Meme')
sisters = ('Maya','Lemy')
siblings = brothers + sisters
print(len(siblings))
parents = ('Mama', 'Papa')
family_members = siblings + parents

#Exercises: Level 2
print(family_members)
fruits = ('mango','oranges','apples','strawberry','banana')
vegetables = ('cabbage','kales','spinach','carrot','tomatoe')
animal_products = ('milk','eggs','bacon','cheese','ghee')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
without_middle_part = food_stuff_lt[:len(food_stuff_lt)//2] + food_stuff_lt[len(food_stuff_lt)//2+1:]
print(without_middle_part)
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
del food_stuff_lt
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)