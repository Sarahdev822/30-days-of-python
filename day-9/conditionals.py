#Exercises: Level 1
from ast import If


age  = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive.')
else:
    print(f'You need {18 - int(age)} more years to learn to drive.')

asb_age = 30
my_age = int(input('Enter your age: '))
if(asb_age > my_age):
    if(asb_age - my_age == 1):
        print(f'You are 1 year older than me.')
    else:
        print(f'You are {asb_age - my_age} years older than me.')
elif(my_age == asb_age):
    print(f'We arw Agemates')
else:
    if(my_age - asb_age == 1):
        print(f'You are 1 year younger than me.')
    else:
        print(f'You are {my_age - asb_age} years younger than me.')

num_one = int(input('Enter number: '))
num_two = int(input('Enter number: '))
if(num_one > num_two):
    print(f'{num_one} is greater than {num_two}')
elif(num_one == num_two):
    print(f'{num_one} is eaqual to {num_two}')
else:
    print(f'{num_one} is smaller than {num_two}')


#Exercises: Level 2
grade = int(input('Enter your grade: '))
if(grade <= 100 and grade >= 90):
    print(f'You have an A')
elif(grade <= 89 and grade >=80):
    print(f'You have a B')
elif(grade <= 79 and grade >= 70):
    print(f'Yooou have a C')
elif(grade <= 69 and grade >= 60):
    print(f'You have a D')
else:
    print(f'You have a D')

autum = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March' , 'April', 'May']
summer = ['June', 'July', 'August']
month = input('Enter the month: ')

if(autum.includes(month)):
    print(f'The season is autum')
elif(winter.includes(month)):
    print(f'The season is winter')
elif(spring.includes(month)):
    print(f'The season is spring')
else:
    print(f'The season is summer')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')
if(fruits.includes(fruit)):
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print('Modified list:', fruits)


#Exercises: Level 3
person={
            'first_name': 'Asabeneh',
            'last_name': 'Yetayeh',
            'age': 250,
            'country': 'Finland',
            'is_married': True,
            'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
            'address': {
                            'street': 'Space street',
                            'zipcode': '02210'
                        }
        }
front_end = ['JavaScript', 'React']
back_end = ['Node', 'Python', 'MongoDB']
if ('skills' in person):
    print(person['skills'][int(len(person['skills']) // 2)])
    if ('Python' in person['skills']):
        print('Python is in the skills list')
    else:
        print('Python is not in the skills list')
    if('JavaScript' in person['skills'] and 'React' in person['skills']):
        print('He is a front end developer')
    elif('Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']):
        print('He is a backend developer')
    else:
        print('unknown title')
else:
    print('Skills not found')

if(person['is_married'] and person['country'] == 'Finland'):
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married.')