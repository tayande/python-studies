# From Day 1 (execution model):

# Write a 3-line script with a deliberate indentation error, and before running it, state exactly what error type Python will throw and why.

# answer
# def name(text: str):
# return text

# text = "In the time of need"
# result = name(text)
# print(result)
# the code above would throw an indentation error.
# below is the correct version of it
# def name(text: str):
#     return text

# text = "In the end of time and by 20 years of time"
# result = name(text)
# print(result)

# From Day 3 (core types & arithmetic):

# -17 // 5 # -4
# -17 % 5 # 3
# 17 % -5 # -3
# 2 ** 10 # 1024
# True + True + True # 3
# int("17.5") — does this work or error? Why? # This will not work because the argument you are trying to convert here does not match the one you are trying to convert to. In essence, the content can be converted to a float rather than an int given that the content is a decimal number.

# From Day 4 (strings):

# Reverse this string using slicing only: "Learning Python"
# answer:
# def reverse(text: str):
#     if text == "":
#         print("text cannot be empty")
#     return text[::-1]
# text = "Learning Python"
# result = reverse(text)
# print(result)


# Given sentence = "the fox runs fast", write the one-liner to get "The Fox Runs Fast" using .split(), .capitalize(), and .join() (no .title() allowed — force yourself through the mechanism again)
# answer:
# def convert(text: str):
#     if text == "":
#         print("text cannot be empty")
#     result = []
#     words = text.split()
#     for word in words:
#         word = word.capitalize()
#         result.append(word)
#     return " ".join(result)

# sentence = "the fox runs fast"
# another = convert(sentence)
# print(another)


# Explain in your own words why "hello".upper (no parentheses) does NOT print "HELLO" if you just type it alone in the REPL
# answer 
# I think that it will not work because the .upper() is a function and all functions have a way they work and how they should be worked with, and using or calling it without the parenthesis may not raise an error but it will not give you the conversion you need, rather it would provide some info about the function.
