#Day 5 exercises
#Level 1 exercises
lst = list()
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(len(days))
first_item = days[0]
middle_item = days[3]
last_item = days[len(days) - 1]
mixed_data_types = [{'name':'Sarah','age':10,'height':1.54},'Married',1453]
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
no_of_companies = len(it_companies)
print(no_of_companies)
first_company = it_companies[0]
middle_company = it_companies[int(len(it_companies) / 2)]
last_company = it_companies[len(it_companies) - 1]
it_companies.insert(2,'Safaricom')
print(it_companies)
it_companies.append('Airtel')
it_companies.insert(int(len(it_companies) / 2),'Mpesa')
print(it_companies)
it_companies[3].upper()
new = '# '.join(str(it_companies).split(', '))
'IBM' in it_companies
it_companies.sort()
it_companies.reverse()
sliced = it_companies[-10:-3]
sliced_middle_company = it_companies.pop(int(len(it_companies) / 2))
it_companies.pop()
it_companies.clear()
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux','Node','Express', 'MongoDB']
full_stack.insert(5,'Python')
full_stack.insert(5,'SQL')
print(full_stack)


#Exercises Level 2
#find the median and the average age of the ages list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
max_age = max(ages)
min_age = min(ages)
median = int((20 + 25) / 2)
total_age = sum(ages)
average_age = total_age / len(ages)
range_of_ages = max(ages) - min(ages)
abs(max_age - average_age) > abs(min_age - average_age)
abs(max_age - average_age) < abs(min_age - average_age)