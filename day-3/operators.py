age = 24
height = 1.75
comp = 1 + 2j
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is ", area)
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is ", area)
print("The perimeter of the rectangle is ", perimeter)
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is ", perimeter)
radius = float(input("Enter radius: "))
area = float(3.14 * radius ** 2)
print("The area of the circle is ", area)
circumference = float(2 * 3.14 * radius)
print("The circumference of the circle is ", circumference)
slope8 = 2
x_intercept = 1
y_intercept = -2
print("The slope of the line is ", slope8)
print("The x-intercept of the line is ", x_intercept)
print("The y-intercept of the line is ", y_intercept)

y1 = 2
y2 = 10
x1 = 2
x2 = 6
slope9 = (y2 - y1) / (x2 - x1)
print("The slope of the line is ", slope9)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("The Euclidean distance between the two points is ", euclidean_distance)

2 == 2
y = 4 ** 2 + 6 * 4 + 9
y = 3 ** 2 + 6 * 3 + 9
y = 7 ** 2 + 6 * 7 + 9

#operators
len('python') != len('dragon')
print('jargon' in 'I hope ths curse is not full of jargon')
print('on' not in 'dragon' and 'jargon')

print(str(float(len('python'))))

#a number is even if
num = int(input("Enter a number: "))
if(num % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")

print(7 // 3 == int(2.7))
print(type('10') == type(10))
print(int('9.8') == 10)

#calculating weekely earnings
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print("Your weekly earning is ", weekly_earning)

#number of seconds someone has lived
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for ", seconds, " seconds")

#Write a Python script that displays the following table
for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3, i**4, i**5)
    