def reverse_list(array):
    results = []
    for i in range(len(array) - 1, -1, -1):
        results.append(array[i])
    return results


def capitalize_list_items(list1):
    capitalized_list = []
    for items in list1:
        capitalized_list.append(items.upper())
    return capitalized_list

def add_items(list,item):
    list.append(item)
    return list

def sum_of_numbers(nums):
    sum = 0
    for num in range(nums + 1):
        sum += num
    return sum

def sum_of_odds (nums):
    sum = 0
    for num in range(nums + 1):
        if(num % 2 != 0):
            sum += num
    return sum


print(sum_of_odds(35))
print(sum_of_numbers(5))
print(add_items(['Potato', 'Tomato', 'Mango', 'Milk'],'Meat'))
print(capitalize_list_items(['sarah','lloyd','edu']))
print(reverse_list([1, 2, 3, 4, 5]))