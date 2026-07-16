# day 4: 
# 1: Reverse a string
print("number 1")
word = "Python"

print(word)
print(word[::-1])
print()
name = "Ayande David Terngu"
print(name)
print(name[::-1])
print()
print("number 2")
# 2: count vowels

sentence = "The quick brown fox"
vowels = "aeiouAEIOU"
count = 0

for char in sentence:
    if char in vowels:
        count = count + 1

print(count)
# using a function to do the same thing:
def counting(text: str):
    vowels = "aeiou"
    count = 0
    new_text = text.lower()
    for char in new_text:
        if char in vowels:
            count += 1
    return count
text = "In the land of myth and a time of magic"
result = counting(text)
print(f"The number of vowels in '{text}' are: {result}")

# 3: Title-case a sentence manually(without using the built-in .title())
print()
print("number 3")
def splitting(text: str):
    nice_text = text.lower()
    splitted_text = nice_text.split()
    for i in range(len(splitted_text)):
        splitted_text[i] = splitted_text[i].capitalize()
    return " ".join(splitted_text)
list = "In the land of myth"
final = splitting(list)
print(final)
print()

# 4: check if a string is a palindrome (reads the same foreward and backward)
print("number 4")
def check_palindrome(text: str):
    cleaned = text.lower()
    return cleaned[::-1]

word = "racecar"
result = check_palindrome(word)
if result == word:
    print("The text is a palindrome")
else:
    print("The text is not a palindrome")    
print()
print("number 5")
# 5: Remove all vowels from a string
def remove(text: str):
    if len(text) == 0:
        print("text cannot be empty")
    result = ""
    vowels = "aeiou"
    for char in text:
        if char in vowels:
            continue
        else:
            result += char
    return result
print(remove("In the land of myth"))
print()
print("number 6")

# 6: count the occurences of a specific word without using .count().
def counting(text: str, target: str):
    if len(text) == 0: 
        print("text cannot be empty")
    if len(target) == 0:
        print("Target word cannot be empty")
    count = 0
    splitted = text.split()
    for word in splitted:
        if word == target:
            count = count + 1
    return count

text = "how many the are in the sentence"
target = "the"
result = counting(text, target)
print(f"'{target}' appears {result} times in '{text}'")
print()
print("number 7")

# 7: Extract the domain from an email address
def check(email: str):
    if len(email) == 0:
        print("please provide an email")
    new_email = email.split("@")
    return new_email[-1]

print(check("ayande@gmail.com"))
# this works just fine but to add more to it

def check(email: str):
    if email == "":
        print("email can not be empty")
    return email.split("@")
email = "ayandedavid2002@gmail.com"
result = check(email)
first_part = result[0]
second_part = result[-1]
print(f"The username in '{email}' is '{first_part}' and the domain is '{second_part}'")
print()
print("number 8")
# 8: check if a string starts and ends with the same character
def check(word: str):
    if word == "":
        print("word cannot be empty")
    if word[0] == word[-1]:
        return "The first character is the same with the last character"
    else:
        return "The first character is not the same with the last one"
print(check("level"))
print(check("now"))
print()