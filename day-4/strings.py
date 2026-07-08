#Day 4 exercises
#string concetation
print('Thirty ' + 'Days ' + 'Of ' + 'Python')
print('Coding ' + 'For ' + 'All')
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print('Coding For all'.capitalize())
print('Coding For All'.title())
print('Coding For All'.swapcase())
string = 'Python For Everyone'.replace('Everyone', 'All')
print(string)
print('Coding For All'.split(' '))
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

#finding the index of character and substrings in strings
sentence = 'Coding For All'
first_character = sentence[0]
print(first_character)
last_index = len(sentence) - 1
print(last_index)
print(sentence[10])
print(sentence.index('C'))
print(sentence.index('F'))
print(sentence.rfind('I'))
sentence2 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence2.index('because'))
print(sentence2.rindex('because'))

#using other string methods to manipulate strings
sentence3 = 'You cannot end a sentence with because because because is a conjunction'
target_words = 'because because because '
start = sentence3.find(target_words)
end = start + len(target_words)
result = sentence3[:start] + sentence3[end:]
print(result)

#finding the first ooccurance of substrings
print(sentence3.find('because'))

sentence4 = 'Coding For All'
print(sentence4.startswith('Coding'))
print(sentence4.endswith('coding'))
word = '   Coding For All      ' 
new_word = word.strip()
print(new_word)
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))

#escape sequence in python
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\nSarah\t25\tKenya\tNairobi')

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {:.0f} meters square.'.format(radius, area))

#using sring formarting methods
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))