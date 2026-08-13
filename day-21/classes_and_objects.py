#Exercises: Level 1
#Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
class Statistics:
  def __init__(self, data):
    self.data = data

  def mean(self):
    return sum(self.data) / len(self.data)

  def sum(self):
    return sum(self.data)

  def min(self):
    return min(self.data)

  def max(self):
    return max(self.data)

  def median(self):
    sorted_data = sorted(self.data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
      return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
      return sorted_data[mid]

  def mode(self):
    frequency = {}
    for num in self.data:
      frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    return modes

  def range(self):
    return max(self.data) - min(self.data)

  def variance(self):
    mean_value = self.mean()
    return sum((x - mean_value) ** 2 for x in self.data) / len(self.data)


  def std(self):
    return self.variance() ** 0.5

  def min_value(self):
    return min(self.data)

  def max_value(self):
    return max(self.data)

  def count(self):
    return len(self.data)

  def percentile(self, p):
    sorted_data = sorted(self.data)
    index = int(p * len(sorted_data))
    return sorted_data[index]

  def var(self):
    mean_value = self.mean()
    return sum((x - mean_value) ** 2 for x in self.data) / len(self.data)

  def freq_dist(self):
    frequency = {}
    for num in self.data:
      frequency[num] = frequency.get(num, 0) + 1
    return frequency

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode())
print('Standard Deviation: ', data.std())
print('Variance: ', data.var())
print('Frequency Distribution: ', data.freq_dist())

#Exercises: Level 2
#Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.
class PersonalAccount:
  def __init__(self, firstname,lastname, income, expenses):
    self.firstname = firstname
    self.lastname = lastname
    self.income = income
    self.expenses = expenses
  
  def total_income(self):
    return sum(self.income.values())

  def total_expense(self):
    return sum(self.expenses.values())

  def account_info(self):
    return f"Account Info: {self.firstname} {self.lastname}, Total Income: {self.total_income()}, Total Expense: {self.total_expense()}"

  def add_income(self, description, amount):
    self.income[description] = amount

  def add_expense(self, description, amount):
    self.expenses[description] = amount

  def account_balance(self):
    return self.total_income() - self.total_expense()