#Exercises: Day 16
#Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
current_date = now.strftime("%d/%m/%Y, %H:%M:%S")

#Today is 5 December, 2019. Change this time string to time.
today = "3 August, 2026"
today_time = datetime.strptime(today, "%d %B, %Y")

#Calculate the time difference between now and new year.
now = datetime(year = 2026, month = 8, day = 3, hour = 9, minute = 28, second = 24)
new_year = datetime(year = 2027, month = 1, day = 1, hour = 0, minute = 0, second = 0)
time_difference = new_year - now

#Calculate the time difference between 1 January 1970 and now.
year_1970 = datetime(year = 1970, month = 1, day = 1, hour = 0, minute = 0, second = 0)
time_difference_1970 = now - year_1970

#Think, what can you use the datetime module for? Examples:
#Time series analysis
#Date and time manipulation
#Adding posts on a blog
