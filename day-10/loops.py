#Exercises: Level 1
for number in range(11):
  print(number)

count = 0
while count <= 10:
  print(count)
  count += 1

for number in range(10, 0, -1):
  print(number)

counter = 10
while counter >= 0:
  print(counter)
  counter -= 1

for t in range(8):
  print('# ' * t)

for t in range(8):
  print('# ' * 7)

for nums in range(11):
  print(f'{nums} x {nums} = {nums * nums}')

languages =  ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in languages:
  print(language)

for num in range(101):
  if(num % 2 == 0):
    print(num)

for num in range(101):
  if(num % 2 != 0):
    print(num)

#Exercices level 2
sum = 0;
sum_of_odds = 0;
sum_of_evens = 0;
for numbers in range(101):
  sum += numbers
  if(numbers % 2 != 0):
    sum_of_odds += numbers
  else:
    sum_of_evens += numbers

print(sum)
print(sum_of_odds)
print(sum_of_evens)
