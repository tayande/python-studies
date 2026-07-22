## Day 1
### Introduction to python
Python is a high level programming language for general-purpose programming. It is an open source, interpreted, object-oriented pragramming language. It was created by Guido Van Rossum. The name python was gotten from a britich sketcy comedy series called "Monty python's flying circus" (MPFC)
## Python indentation
It is seen as a white space in a text. In other languages, indentation is used to make code readable but in python, indentation is used to create blocks of code. 
## data types
### bool
### int
### str
### float
### list
This is seen as an ordered collection which allows to store different data type items. A list is similar to array in JS na slice is GO. 
### Dictionary
Works just like Go's maps
### Tuple
A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.
### Set
A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an odered collection of items. Like in maths, set in python astores only unique items.
## Day 2: Variable and built-in functions
### built-in functions
In python, there are many built-in functions that make working or writing python code easier. these built-ins have certains features of how they are used and they must be used in that manner for them to perform as expected. With a built-in fucntion, you can use a module embedded in it without importing an external package for your program. Using them while writting different programs in python would provide more info about the concept.
### Variables
They store data in a computer memory. Mnemonic variables are recommended while working with variables. *** A mnemonic variable *** is a variable name that can be easily remembered and associated. In essence, such a variable describes it's meaning, and what it does to even someone who is not a programmer. If such varibles names are used, it would be easy for another programmer to work on the same project with a different one as well. A varible refers to the memory address to which data is stored.
### Python Variable Name Rules
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables
*** note *** that even though you can follow any of the naming rules to name your variables, it is necessary to understand that the standard naming other programmers use is the snake case style shown below: 
- variable_name
For a fucntion, the argument it takes is said to be the value which can be passed or put inside the function parenthesis. for instance:
- print("Ayande Terngu David")
- len("Terngu")
### Declaring multiple varibles on a single line.
Multiple varibles can be declared on the same line as shown below:
```python
first_name, last_name, country, age, is_married = 'Ayande', 'Terngu', 'Canada', 25, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```
### Getting user input
The built-in function used to obtain user input from the terminal is the input() function. Here is a similar syntax  of how it is used:
```python
name = input("Enter you name: ")
age = int(input("How old are you? "))
```
###  Data types
Data types helps tell us what a value of a variable really is, how to work with them and how they behave (it's properties)
The data type of a value can be checked using the type() function. Here is a syntax of how it is used:
```python
print(type("Terngu"))
```
### Casting
This is defined as the process of converting one data type to another. In essence, if you have an int, and you need to behave as a float, you can cast it to become the float you need it to be. There are special functions that allow us to do the casting as well and they include:
- int() - converting to integers
- float() - converting to decimals
- str() - converting or casting to strings
- list() - converting or casting to list
### Numbers in python
We have different number types in python and they include:
- integers: These are refered to as whole numbers
- float: Theser are refered to as numbers with decimal points
- complex numbers: for example: 1 + j, 2 + 4j, 1- 1j