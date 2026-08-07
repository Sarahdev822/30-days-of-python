import re
from collections import Counter
#What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = re.findall(r'\w+', paragraph.lower())
words_count = Counter(words)
most_common_word, frequency = words_count.most_common(1)[0]
print(f"Most frequent word: '{most_common_word}' (appears {frequency} times)")

#The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
numbers = re.findall(r'-?\d+', text)
distance = max(map(int, numbers)) - min(map(int, numbers))
print(distance)

#Exercises: Level 2
#Write a pattern which identifies if a string is a valid python variable
is_valid_variable_name = lambda name: bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name))
print(is_valid_variable_name('first_name')) 
print(is_valid_variable_name('first-name'))

#Exercises: Level 3
#Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
cleaned_sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)
words = re.findall(r'\w+', cleaned_sentence.lower())
words_count = Counter(words)
three_most_frequent = words_count.most_common(3)
for word, frequency in three_most_frequent:
    print(f"'{word}': {frequency}")

