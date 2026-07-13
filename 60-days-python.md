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