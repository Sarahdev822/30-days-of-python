#Exercises: Level 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
length_of_the_it_companies = len(it_companies)
it_companies.add('Twitter')
it_companies.update(['Safaricom', 'Airtel', 'Telkom'])
it_companies.remove('Facebook')
#Remove returns an error if the item does not exist. discard() removes an item if it exists, and does nothing if it does not exist.


#Exercises: Level 2
joined_a_and_b = A.union(B)
a_intersection_b = A.intersection(B)
a_is_subset_of_b = A.issubset(B)
a_and_b_disjoint = A.isdisjoint(B)
a_with_b = A.union(B)
b_with_a = B.union(A)
a_and_b_symmetric_diff = A.symmetric_difference(B)
del A
del B
del it_companies


#Exercises: Level 3
set_of_age = set(age)
length_of_set_of_age = len(set_of_age)
length_of_age = len(age)
length_of_set_of_age == length_of_age

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuples is a collection which is ordered and unchangeable. Allows duplicate members.
#Sets is a collection which is unordered and unindexed. No duplicate members.
#Strings are arrays of uniode characters.

sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
print(unique_words)