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