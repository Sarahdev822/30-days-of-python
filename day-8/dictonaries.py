dog = {
  'name':'Tom',
  'color':'brown',
  'legs':4,
  'age':5
}

student = {
  'first_name':'Sarah',
  'last_name':'Njagi',
  'gender':'female',
  'age':20,
  'is_married':False,
  'skills':['Python','JavaScript','HTML','React','CSS'],
  'country':'Kenya',
  'city':'Nairobi',
  'address':'P.O Box 12345-00100'
}

length_of_student = len(student)
value_of_skills = student['skills']
print(type(value_of_skills))
value_of_skills.append('Django')
value_of_skills.append('Flask')
print(student['skills'])
print(dog.keys())
print(student.keys())
print(dog.values())
print(student.values())
dog__list_tuple = dog.items()
print(dog__list_tuple)
print(student.items())
del dog['age']
del dog