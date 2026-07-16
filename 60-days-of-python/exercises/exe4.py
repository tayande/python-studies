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

# 5: Remove all vowels from a string
