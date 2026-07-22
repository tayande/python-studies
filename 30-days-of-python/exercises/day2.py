# Exercises: level 1
# Declare a first name variable and assign a value to it
first_name = "Terngu"
# Declare a last name variable and assign a value to it
last_name = "Ayande"
# Declare a full name variable and assign a value to it
full_name = "Terngu Ayande"
# Declare a country variable and assign a value to it
country = "Nigeria"
# Declare a city variable and assign a value to it
city = "Makurdi"
# Declare an age variable and assign a value to it
age = 24
# Declare a year variable and assign a value to it
year = 2026
# Declare a variable is_married and assign a value to it
is_married = False
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = "No"
# Declare multiple variables on one line
first, second, third, fourth, fifth = "1st", "2nd", "3rd", "4th", "5th"

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(first))
print(type(second))
print(type(third))
print(type(fourth))
print(type(fifth))
print()

# Using the len() built-in function, find the length of your first name
print(len(first_name))
print()

# Compare the length of your first name and your last name
if len(first_name) > len(last_name):
    print("first name is longer than last name")
if len(first_name) < len(last_name):
    print("last name is longer than first name")
if len(first_name) == len(last_name):
    print("first name if equal in length to last name")
print()

# Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4
# Add num_one and num_two and assign the value to a variable total
variable_total = num_one + num_two
print(variable_total)
# Subtract num_two from num_one and assign the value to a variable diff
variable_diff = num_one - num_two
print(variable_diff)
# Multiply num_two and num_one and assign the value to a variable product
variable_product = num_one * num_two
print(variable_product)
# Divide num_one by num_two and assign the value to a variable division
varibale_division = num_one / num_two
print(varibale_division)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
variable_remainder = num_one % num_two
print(variable_remainder)
# Calculate num_one to the power of num_two and assign the value to a variable exp
variable_exp = num_one ** num_two
print(variable_exp)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
variable_floor_division = num_one // num_two
print(variable_floor_division)
print()

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30
area = 3.142 * radius ** 2
result = format(area, ".3g")
print(area) 
print(f"{area:.2g}")
print(result)
print()
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
radius = 30
circumference = 2 * 3.142 * radius
result = format(circumference, ".3g")
print(f"The circumference of a circle with radius {radius} is {result}")
print()
# Take radius as user input and calculate the area.
radius = int(input("Enter the radius of a circle whose area you want to compute: "))
area = 3.142 * radius ** 2
result = format(area, ".3g")
print(f"For a circle of radius {radius}, the area is {result} as rounded up by to 2 significant figures")
print()

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your Last name: ")
age = int(input("Enter your age: "))
country = input("What is your nationality? ")
print(f"Your name is {first_name} {last_name}, you are {age} years old and you are from {country}.")
print()
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
print("====DONE====")
