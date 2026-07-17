# python studies
## python introduction
Python is a popular programming language. It was created by Guido van Rossum, and it was realease in 1991. It is used for:
- web development (server-side)
- system scripting: This is defined as the process of writing scripts or code in scripting languages to automate repetitive tasks and manage operating systems.
- software develpment
- mathematics
### uses of python
- python can be used to handle big data 
- python can be used to perform complex mathematics
- python can be used to create web applications
- python can be used to connect database systems. 
- python can also be used to read and modify files
### why python
- It works on different platforms (windows, Mac, Linux, etc)
- It's syntax is easy and simple to understand
- It runs on an interpreter system, meaning that code can be executed line by line as soon as it is written, and catching bugs and mistakes is very easy and quick.
### python syntax compared to other programming languages
- It was designed for readability, and has some similarities to the english language with influence from mathematics.
- It relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other languages often use curly braces.
## getting started
### python install
Some computers already have python pre-installed on them so to know if python is available on  system, run the following command on the terminal:
- python --version or pytho3 --version
Then if it's not, you can download it using:
-  https://www.python.org/
But if python it's installed, you can go ahead and write and run a python program. To run it, use:
- python <filename> or python3 <filename>
## python syntax
### python indentation
Indentation refers to the spaces at the beginning of a code line. In other programming languages, indentation is used to make code readable while in python, it is used to define a block of code. The number of spaces that show indentation in python is optional depending on what the programmer wants but the default number of spaces used in python is four (4). But once there is no indentation, python throws an error. 
### python variables
In python, a variable is created when you assign a value to it. For instace:
` x = 5`
` y = "Hello, World!"`
python has no command for declaring a variable
### comments
Comments start with a #, and python will render the rest of the line as a comment. Unlike other programming laguages, python does not have a special syntax to write a multiline comments, you need to add the # at the beginning of every line you want to be seen by python as a comment.
## python statements
A computer program is a list of "instructions" to be executed by a computer. In a programming language, these programming instructions are called statements. For instance: the following statement prints the text "Python is fun!" to the screen:
`print("Python is fun!")`
The above is termed a statement and when you have alot of them telling the computer what to do, you call them many statemensti n python. They usually end when the line ends, and they are execute one by one, in the same order as they are written.
### semicolons (optional, rarely used)
They are optional in python, you can write multiple statements on the same line by separating them with ";". but this is not oftenly used because it makes it hard to read code that is written with it.
## python output/print
### print text
The function that allows for text to be printed out is: 
` print()`
It takes in what you want to be printed and prints it.
### print without a new line
By default, print() ends with with a newline. But if you want to print without a new line, you can use *** end *** parameter. For instance:
` print("hello world", end=" ")`
The above text will be printed without a new line.
### print numbers
Numbers can still be printed using the same function. The difference here is that unlike text, you would not have to put the number surrounded by quotes.
### mix text and numbers
You can also combine both text and numbers and print them in the same sentece. Here is a similar syntax:
` print("I am", 25, "years old.")`
### casting
This is the process of specifying the data type of a variable while creating and storing a value to it. for instance:
` x = str(3) # x will be '3'`
` y = int(3) # y will be 3`
` z = float(3) # z will be 3.0`
### get the type
To get the type of a variable, you can do it using the type() function. For instance:
- print(type(x)) 
The result would be the data type of the variable x that would be printed. 
### case sensitive
variable names are case-sensitive, for you to access or use a variable, you must call it by the exact name and cases you created it to be. For instance: 
- a is not the same as A
- x is not the same as X
### variable names
there are certain rules governing the naming of variables and they include:
- a variable name must start with a letter or an underscore.
- a variable name cannot start with a number
- a variable name can only contain alpha-numeric characters and underscores
- a variable name is case-sensitive
- a variable name cannot be any of the python keywords
### multi words variable names
variable names with more than one word have a specific pattern of how they are named or given. They take (first) the camel case style, for instance:
`myVariableName = "John"`
(second), they take the pascal case, for instance:
` MyVariableName = "John"`
(third), they take the snake case, for instance:
` my_variable_name = "John"`
## Assign multiple values
more than one value can be assigned to it's variable on the same line. For instance:
` x, y, z = "Orange", "banana", "cherry"`
### one value to multiple variables
You can also assign the same value to multiple variables in one line. For instance:
`x = y = z = "Orange"`
### unpack a collection
Unpacking is a process in python whereby you have a collection of values in a list, tuple etc, and you extract the values into variables. For instance:
```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
## global variables
```
These are varibles that are created outside of a function. A global variable can be used by anyone, both inside and outside of functions. If you create another variable in a function that carries the same name as a global variable, the one you created in the function will be used once you call that variable, but outside that very function you created the function, it will be the global varible that would be called once you mention the name of the variable.
### the global keyword
Normally, when you create a variable inside a function, such a variable is said to be local, and can only be used inside that function. To create a global variable inside a function, you can use the global keyword. Here is a sytax of it:

```python
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```
In this example, you will understand that the x variable is made global using the global keyword and then it can be used in another function as well and it will still be fine. And also, when you have a global variable and you want to change the value of the variable, you can still use the global keyword to change or alter the value of that variable. for instance:
```python
x = "awesome"
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("python is " + x)
```
### Python data types
A data type is what tells python the kind a value a variable is carrying, how it can be used and what operations to perform on it. For instance, assuming a variable is carrying a value and the type of that value is an int, that value can only undergo a given number of operations based on how python allows int to be treated, it can not be treated or worked with like a str or a bool.
### Build-in data types in python 
Python has the following data types which are built-in by default, and they are grouped as follows:
Text Type: 	    str
Numeric Types: 	int, float, complex
Sequence Types: list, tuple, range
Mapping Type: 	dict
Set Types: 	    set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	    NoneType
### Getting the type
You can get the data type of a variable by using the type() function. 
### Python numbers
There are three numeric types in python:
- int for instance: x = 1
- float for instance y = 2.8
- complex for instance z = 1j
#### Int
This is a whole number, positive or negative, without decimals, of unlimited length. For instance
- 1
- 34543524543
- -34532
#### Float
Float, or floating point number is a number, positive or negative, containing one or more decimals. for instance:
- 1.23
- 1.0
- -234.34
float can also be scientific numbers with an "e" to indicate the power of 10. For instance:
#### complex
They are written with a "j" as the imaginary part: for instance:
- x = 3 + 5j
- y = 5j
- z = -5j
#### type conversion
this is an operation that is done on a variable to change the data type of its value. for instance:
```python
x = 1
y = 2.8
z = 1j
# to convert from int to float:
a = float(x)
# to convert from float to int:
b = int(y)
# to convert from int to complex:
c = complex(x)
```
#### Random number
Pythonn does not have a random() function to make a random number, but it does have a built-in module called random that can be used to make random numbers. for instance:
```python
import random

print(random.randrange(1, 10))
```

### Python casting
This is defined as the process of explicitly converting the data type of a value to another, producing a new value of the target type. It is done by calling a conversion function: int(), str(), float(), etc, rather than happening automatically. For instance:
```python
>>> age = "25"
>>> int(age)
25
>>> age
'25'
```
### Python strings
In python, a string is an unchangeable or immutable sequence that is seen and treated by python as a text. It is either surrounded by double or single quotes.
### Multiline strings
A multiline string is assigned by surrounding it with three quotes, either single or double.
For instance:
```python
>>> name = """In the land of myth
... and a time of magic
... the destiny of a great kingdom 
... lies on the shoulders of a young boy
... his name, Merlin!!!"""
>>> print(name)
In the land of myth
and a time of magic
the destiny of a great kingdom 
lies on the shoulders of a young boy
his name, Merlin!!!
>>> 
```
### looping through a string
Since strings are arrays, we can loop through them using the for loop:
```python
name = "Ayande"
for i, char in enumerate(name):
    print(f"{i}: {char}")
```
And:
```python
name = "David"
for char in name:
    print(char)
```
### check string
To check if a certain phrase or a character is present in a string, we can use the keyword "in". And an if statement, you would be able to check is an expression is in a text or not. for instance:
```python
text = "The best things in life are free!"
if "free" in text:
    print("Yes, 'free' is present.")
else:
    print("No, 'free' is not present.")
```
Also, if you want to check if it does not exist or not:
```python
text = "In the land of myth"
if "the" not in text:
    print("'The' is not present")
```
### python escape characters
An escape character is a backlash \ followed by the character you want to insert.