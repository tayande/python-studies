# 60 days python mastery roadmap
## Day 1: What python is, environment and execution model
### Interpreted vs Compiled
The primary difference between interpreted and compiled languages is when and how the human-readable source code is translated into machine-readable binary code. Compiled langauges translate the entire codebase into machine code all at once before execution, creating a standalone file. While an Interpreted langaue translates and executes the source code line-by-line on fly during run time. Here is a real world instance of it:
- Compile language can be picured in a spanish book that needs to be read by an english tutor, and he tutor takes the entire spanish book, translates it into english then goes ahead to read it out to the audience.
- Interpreted language can be pictured in the same scenario but in a different manner in the sense that that tutor instead of him or her to translates the entire book first before reading it, it's more like as soon as the live spanish person or mic is on and speaking the spanish, the tutor on the other hand is interpreting what the spanish person is saying word for word. 
### The clearer picture
There is python which is the programming language (set of rules and instructions) and there is CPython which is the bridge that connects the theoritical python language to the practical concept of compilation and interpretation. Cpython is the actual software engine that reads and executes that python code. 
So this Cpython reads your .py file and compiles it to bytecode(not machine code, lower-level intermediate representation), then an interpreter (which is a virtual machine written in C) executes that bytecode line by line, on the fly. Anyone running your python script needs python installed on their computer. 
### CPython, the REPL, and running code three ways
CPython is just the name of the standard python interpreter (written in C). There are other implementations such as Jython, PyPy, but the default one is the CPython unless you specify otherwise.
### Three ways to run Python.
- As a script file (like go run file): python3 file
- The REPL (Real-Eval-Print-Loop): This method is used for testing small ideas without writing a whole file. This way is literally amazing too, here is what you need to do to be able to run a python code in this manner: First of all, run the command: python3 on the terminal, you will get something like this: >>>. That is when you start writing your code, you can write as you do in the normal .py file, but the difference is after each line of code, you need to press enter and then another line of >>> comes up for you to coninue writing. You will get the results in the terminal in real time and when you are done, you can just write exit() in the >>> line and the REPL closes fine. Another thing to take note of when using this is that you do not necssarily need to write a statement with print for it to be printed to the terminal, this is becuase, REPL echos it's statements to the terminal automatically.
- python3 -c: This runs a one-liner (one line of code) directly from the shell, not file needed. Here is a syntax to follow:
`python3 -c "print('hello')"`
To be able to write multile statements with this method, you have to seperate each stated by a semi-colon (;), but you can write as many statements as you want, so far as they are separeted by the (;) everything will run fine.
### Indentation as syntax 
In python, indentation is the block structur. There are no braces, the interpreter uses whitespace to know where a block starts and ends. For instance:
```python
def greet(name):
    if name:
        print(f"Hello, {name}")
    else:
        print("Hello, stranger")

```
*** rules that matter ***
- standard is 4 spaces per indentation level. Not tabs, mixing tabs and spaces will cause errors.
- Everything at the same logical block must be indented identically. One line off by one space relative to its siblings will cause an indentation error.
- The colon at the end of if, def, for, while, class etc signals that "an indentation block follows". Forgetting the colon is a classic-day-one mistake.
## exercises
>>> done 
### Rounding up day one
If you observe, when a python script or code is running and along the line there is an error, the correct lines before the error will be printed out until it gets to where the error occured and that is where you will see the error message instead of the actual output that was expected. This is the cleares picture that sets python apart from other languages which are said to be compile languages. For instance, when running GO code, if there is an error at all in the program, it won't even run in the first place until you correct the error, this shows how go first of all translates the whole human code into machine code and checks for errors at that translation time, before a go code executes, there are usually not errors, if not it won't execute in the first place. So this scenario simplifies the whole compile and interpreted languages stuff. Here is what happens in python: when you write a program in python in a .py file, the CPython takes the .py file, reads from top to bottom, converts it to bytecode as it reads and then immediately executes the bytecode. 
#### Why REPL matter beyond "it's cool"?
Because it's direct window into that one-condition-motion model. Every line you type gets compiled-and-executed immediatel, one line at a time, and the result is kep alive in the lines.
### Casting
This is defined as the process of explicitly converting the data type of a value to another one, producing a new value of the target type, done by calling a conversion functio: int(), str(), float(), etc, rather than happening automatially.
## Day 2: Variable and dynamic typing
### Varible assignment. No declarations, period
In go, creating a variable allows you to creat it and at the same time, assing the data type to it that is unchanged, but in python the declaration is a bit different, python has no declaration step at all, assignment is creation. For instance: ` age = 24 `.
This single line does everything. it creates the age variable, creates the integer value of 24 sonewhere in memory, and makes age point at it. Note that python already knows that the age is an int. 
### Python variables
In python, a variable is simply said to be a container that holds a particular value with a given data type. It is more like an object that points to a particular value in memory and uses that value whenever it likes. The variable name does not own a fixed size slot (value), but it's just a reference to it. 
### Multiple names can point at the same object simultaneously
```python
>>> a = [1, 2, 3]
>>> b = a
>>> b.append(4)
>>> a
[1, 2, 3, 4]
```
What happened here was that the b did not copy the a's content, it made b a second object on it's own but then it is pointing at the same content as a or it has the same content just as a.
### Dynamic vs Go's static typing
- Go is statically typed: This means that data types are fixed and checked before the program runs, at compile time. The compiler refuses to build if types don't line up.
- Python is dynamically typed: types are checked while the program runs, at the moment each line actually executes. There is no seperate check-everything-first phase.
### type(). Checking what an object actaully is, live.
This function: type(), is used to check or ask what kind of value or object is this, right now, at this moment. This means that it is only at the moment you use it that it will give you the data type of such an object, and that object may change later on, and once it changes, using type() on it again will still give you the data type of it at that particulart time, and this time, it might be different from the earlier one, since you changed the type. For instance:
```python
>>> type(25)
<class 'int'>
>>> type(3.14)
>class 'float'
>>> type("hello")
<class 'st'>
>>> type([1, 2, 3])
<class 'list'>
```
### Duck typing: The philosophy behind why python does not care about declared types.
*** If it walks like a duck and quacks like a duck, then it is a duck.*** 
Python does not care what data type something or an object is, it only cares whether such an object supports the operations and behaviours you're trying to use it for, at the moment you use it. For instance:
```python
def describe(thing):
    print(f"Length is {len(thing)}")

describe("hello")     # str has a length → works
describe([1, 2, 3])   # list has a length → works
describe({"a": 1})    # dict has a length → works
describe(42)          # int has NO length → crashes
```
The function here which is describe does not care whether an object is an int, or float, or str, it just calls the len(), on it and if the object supports the operation, then the code runs, if it does not, then you get an error. *** duck typing *** cares about capability and not declared identity. How a variable is declared or named does not really matter, it is how such a variable can be used that matters. By word of definition: 
*** duck typing *** is a programming concept where an object's suitability is determined by the presencce of certain properties or characteristics, rather than it actual inheritance or class type, or naming or data type. The name comes from the phrase "if it walks like a duck and quacks like a duck, then it must be a duck".
### Multiple assignment
Python allows for the assignment of more than one variable in a single line, matching values to names by position. For instance 
```python
x, y, z = 1, 2, 3
print(x, y, z) # 1 2 3
```
You can also assign the same value to multiple names at once: 
```python
x = y = z = 0
print(x, y, z) # 0 0 0
```
### The classic swap
for instance:
```python
a = 1
b = 2
a, b = b, a
print(a, b)   # 2 1
```
## Day 3: Core data types
### int
In Go, integers have fixed bit-widths which include: int8, int32, and int64, and if a value contained in a variable exceeds this width, you get an overflow(silent sources of bugs). However, in python, int covers for all integers and can contain all numbers negative or positive so far as they are whole numbers and not decimals.
### float
This has or carries the same idea and work ethics like the int. All decimal numbers can be contained in the float, negatve or positive so far as they have a decimal point in them.
### str
This refers to all strings, (which can be defined as an immutable/unchangeable sequence of unicode characters used to handle textual data). Or simply: (a string is an unchangeabel sequence of characters seen and treated as texts).
Python strings have something unique, they support some arithmetic operations which are:
- concatenation:= Done with the + sign
for instance:
```python
>>> "david" + " " + "ayande"
'david ayande'
```
- repetation:= Done with the * sign
for instance:
```python 
>>> "ha" * 3
'hahaha'
```
### bool
This data type is technically a subclass of int.
From the knowledge of Go, bools values are either True of False and it's also the same with python as well, however, those in python here behave a bit different from those of Go.
Bool in python is a subclass of int where True behaves as 1 and False behaves as 0
### None
This is similar to Go's nil but different in how they are used. None is python's absence of a value. The difference between None and Go's nil is that nil can only be used or applied to specific types, such as functions, slices, maps, pointers and interfaces. A plain int in Go can never be nil, it won't even compile in the first place, if a value is not set, it defaults to 0 which is the zero value of int. while None is a single, universal singleton object that any variable can point to, regardless of what it would otherwise hold. for instance:
```python
>>> x = None
>>> type(x)
<class 'NoneType'>
>>> x = 5
>>> x = None   # This is totally fine, because any variable can go back to None 
```
*** note ***
The only way to ckeck for a none value is: is and not: ==:
```python
>>> x = None
>>> x is None
True
```
And also, python has no concept of a zero value. In go, if you declare a variable and not assign a value to it, it would assume the zero value of it's data type, but in python, if you don't assign a value to a declared variable, then there would be an error and if you want a variable to carry the None value, you have to explicitly say so or make it so.
### Type coercion rules
Coercion if the a process where by python allows mixing types in one operation.
#### Numeric coercion
This is when you mix ints with values of different or other data types and it still works. For instance:
```python
>>> 5 + 3.0     # int + float → float
8.0
>>> True + 5    # bool + int → int
6
>>> True + 3.0  # bool + float → float
4.0
```
### Arithmetic operators
- addition: + 
- subtraction: - 
- multiplication: *
- true division: / (7 / 32.3333333333333335)
- floor division: // (7 // 32)
- modulo (remainder): % (7 % 31)
- exponentiation: ** (7 ** 3343)
## Day 4: Strings
A string is defined as an unchangeable sequence that is treated and seen as a text.
### strings literals
Python allows the use of single and double quotes to literally describe a string. For instance:
- name = "Ayande"
- name = 'David'
*** There is another behavior that strings in python allows: ***
Here is a syntax of it:
- quote = "It's a nice day"
- quote = 'She said "hello"'
If you look clearly at the examples above, go cannot just allow such a behaviour unless you use a formating verb to write something like this especially the second example. That is bacause go only uses the double quotes to define it's strings.
### f-strings
This works the same with Go's fmt.Sprintf, but embedded directly. Just like you use formatting verbs in go, python's f-strings embed the actual expressions directly inside the string, prefixed with f: For instance:
- 
```python
result = f"Hello, {name}! You are {age} years old"
```
The variable result has now become one that contains the expression as written and shown above.
Between the braces, you can put any valid expression inside not just a varible name, function calls, arithmetics, method calls, would all work. 
### Formatting specifiers
This is used for controlling decimal places, padding etc. F-strings use a (:) followed by a format spec, conceptually similar to Go's verb flags but different syntax:
```python
>>> pi = 3.14159265
>>> f"{pi:.2f}"          # 2 decimal places
'3.14'
>>> f"{1000000:,}"       # thousands separator
'1,000,000'
>>> f"{5:03d}"           # zero-padded to 3 digits
'005'
```
### Escape sequences
```python
>>> print("Line one\nLine two")
Line one
Line two
>>> print("Tab\tstop")
Tab	stop
>>> print("Quote: \"hello\"")
Quote: "hello"
>>> print("Backslash: \\")
Backslash: \
```
- \n: newline
- \t: tab
- \\: literal backslash
- \" and \': escape quotes
They are all identical to Go's escape sequences.
### Raw strings
They are prefix with r to disable escape processing entirely, useful for regex patterns or windows file paths. For instance:
```python
>>> print(r"C:\new_folder\test")
C:\new_folder\test
>>> print("C:\new_folder\test")
C:
ew_folder	est          # \n and \t got interpreted as escapes — broken!
```
### Multiline strings. Triple quotes
This works just like how the println does in golang. for instance, you have to write three statements on three individual lines and once you use the println function, your statements would be written just how you want them to, but in python, you can write the three statements in the manner you want them to appear when printed and then surround them with tripple double quotes or tripple single quotes and it would work fine. Here is a similar syntax:
```python
>>> message = """This is line one
... This is line two
... This is line three"""
>>> print(message)
This is line one
This is line two
This is line three
>>> 
```
Tripple double quotes or triple single quotes lets a string span multiple lines literally, preserving the newlines exactly as typed.
### Indexing
Strings are indexed sequences which means a string's characters can be accessed by their respective indexes.
```python
>>> s = "Python"
>>> s[0]
'P'
>>> s[5]
'n'
```
### Negative indexing
just like the first index starts from 0, then the second 1, the third 2 and so on, starting the count of indexing from behind (that is from the end of the string to the beginning), the last index is -1, the second to the last is -2 and so on.
```python
>>> name = "python"
>>> name[-1]
'n'
>>> name[-2]
'o'
```
### Slicing 
Basic slice: s[start:stop]. This extracts s substing from start up to (not including) stop. Here is a similar syntax:
```python
>>> s = "Python"
>>> s[1:4]
'yth'
```
### Omitting start or stop
```python
>>> s[:3]      # from start through index 2 which is the same as starting from the begining and stoping on character before the third index
'Pyt'
>>> s[3:]      # from index 3 to the end
'hon'
>>> s[:]       # the whole string (a full copy)
'Python'
```
### The third piece-step
```python
>>> s[::2]     # every 2nd character, from start to end
'Pto'
>>> s[1::2]    # every 2nd character, starting at index 1
'yhn'
```
### Reversing a string
`s[::-1]` is used in python to reverse a string.
```python
>>> s[::-1]
'nohtyP'
```
### Negative indeces work inside slices too
```python
>>> s[-3:]     # last 3 characters
'hon'
>>> s[:-1]     # everything except the last character
'Pytho'
```
*** note ***
slicing never gives an error in python, it just works with what exists.
### Common string methods
strings in python come with built in methods (functions attached to the string object itself, called with .methodname())
### .upper() / .lower(): case conversion
```python
>>> "python".upper()
'PYTHON'
>>> "PYTHON".lower()
'python'
```
### .strip(): removes leading/trailing whitespace (or specified characters)
```python
>>> "   hello   ".strip()
'hello'
>>> "xxhelloxx".strip("x")
'hello'
```
Related: .lstrip() (left only), .rstrip() (right only).
### .replace(old, new)
This function swaps all occurrences:
```python
>>> "I like G".replace("Go", "Python")
'I like Python'
```
### .find(substring)
This function returns the index of the first match, or -1 if not found:
```python
>>> name = "humble"
>>> name.find("mb")
2
>>> name.find("xy")
-1
```
It returns -1 on failure rather than raising an error.
### .split(seperator)
This is used to break strings into a list of substrings:
```python
>>> "one,two,three".split(",")
['one', 'two', 'three']
>>> "hello world foo".split()     # no argument = split on any whitespace
['hello', 'world', 'foo']
```
If no argument is provided in the function, then it would split by whitespaces. (working just like strings.Fields from Go)
### .join(interable)
This function works as a reverse of .split(). You call .join() on the seperator, passing the list as the argument:
```python
>>> ", ".join(["one", "two", "three"])
'one, two, three'
```
It's read as, "take the string, and use it to join together the items in this list".
*** note *** since strings are immutable, any one of these methods returns a brand-new string, none of them modify the original one.
## Day 5: I/O operators
### print()
This works like Go's fmt.Println() but it is more powerful than it. It just takes in an argument you wish to display or print out and it does it's job.
### sep
This controls what goes between multiple printed items. (Default is a single space). Here is a syntax:
```python 
>>> print("a", "b", "c")
a b c
>>> print("a", "b", "c", sep="-")
a-b-c
```
Go's fmt.Println() always joins arguments with a single space, no exceptions, but using both print() and sep in python would allow you specify what is it you want to seperate or join your argumenst together as you print them out.
### end
This controls what gets printed after everything, instead of the default trailing newline. Here is a syntax of how it is used:
```python
>>> print("hello", end="")
hello>>> print("world")     # note: no newline happened after "hello"
helloworld
>>> print("hello", end=" | ")
hello |
```
In go, you have the fmt.Println() that always give a newline at the end of a printed argument, and when you don't want one, you have to explicitly tell by using the fmt.Print() instead, but python gives one powerful output tool that allows you to modify and work with your arguments to be printed just how you want them to. For instance:
```python
>>> for i in range(3):
...     print(i, end=" ")
0 1 2
```
You can combine both, and mix in as many positional values as required:
```python
>>> print("x", "y", "z", sep=", ", end=".\n")
x, y, z.
```
### input()
This is the function that is used to read user input mainly from the terminal. for instance:
```python
>>> name = input("Enter your name: ")
Enter your name: Ayande
>>> name
'Ayande'
```
input() displays the prompt string but it's not necessary, you can call input() with no argument at all and it would still work fine, it waits for the user to input anything at all and then press enter, and it returns whatever the user entered or typed.
One thing worth taking note of is that input() returns a string, no matter what the user types. For instance you need the user to input his age and of course age is always a number, but input() would receive it as a string anyways, it is when you want to use it in your program that you have to convert it to an int and then use it as you want. Here is a syntax of how to convert an input from string to int:
```python
age = int(input("Enter your age: "))
```
### comparison operators
The comparison operators in python are basically the same to those in go and they behave the same way too. They include:
```python
==   equal to
!=   not equal to
<    less than
>    greater than
<=   less than or equal to
>=   greater than or equal to
```
### Logical operators
These are not symbols, theses are: and/or/not
- and : &&
- or : ||
- not : !
Python uses english words instead of symbolic operators here. so always take note, instead of trying to use the symbols, use the english letters for them and they would work fine.
There is another behaviour this operands have, "or" returns the first truthy value it finds (or the last value if none are truth), while "and" returns the first falsy value it finds (or the last value, if all are truth). 
### Chained comparisons
In Go, you cannot chain comparisons but its done in python:
```python
>>> x = 5
>>> 1 < x < 10
True
```
