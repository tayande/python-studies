# day 5
# Exercise 1 — Interactive input/print scripts
# Write a short script that:

# Asks for the user's name and age via input()
# Casts age to int
# Prints a sentence using an f-string combining both
# On a second line, prints the user's name three times, separated by " | ", using a single print() call with sep (hint: print(name, name, name, sep=" | "))
# Prints "Done!" on the same line as the previous output rather than a new line — meaning the previous print call needs end="" instead of the default newline, and this final print should immediately follow it with no leading newline
name = input("Enter you name: ")
age = int(input("Enter you age: "))
new_name = name.title()
print(f"Your name is {new_name} and you are {age} years old")
print(new_name, new_name, new_name, sep=" | ")


# Exercise 2 
# Before running each, predict True or False:
# python1.  bool(0)
# 2.  bool("")
# 3.  bool(None)
# 4.  bool([])
# 5.  bool("0")
# 6.  bool(" ")
# 7.  bool([0])
# 8.  bool(0.0)
# 9.  0 or "backup"
# 10. "" and "unreachable"
>>> bool(0)
False
>>> bool("")
False
>>> bool(None)
False
>>> bool([])
False
>>> bool("0")
True
>>> bool(" ")
True
>>> bool([0])
True
>>> bool(0.0)
False
>>> 0 or "backup"
'backup'
>>> "" and "unreachable"
''