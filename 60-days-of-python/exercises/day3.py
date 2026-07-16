# day 3: exercise 1
# predict mixed-type arithmetic outputs
# write down your prediction for both the value and whether it errors, before running each:
1.  10 + 3.5 # 13.5 (correct)
2.  10 / 3 # 3.3333 (correct)
3.  10 // 3 # 3 (correct)
4.  -10 // 3 # -4 (correct)
5.  10 % 3 # 1 (correct)
6.  -10 % 3 # 2 (correct)
7.  True + True # 2 (correct)
8.  10 ** 0.5 # 3.162 (correct)
9.  "5" + 5 # error (correct)
10. 5 * "ab" # 'ababababab' (correct)


# exercise two
# write a short standalone line covering each of these conversions, and predict the result before running.
int("42")
int(42.9)
int("42.9")     # this one should error — think about why, tied to the ValueError rule from Day 1's casting lesson
float("3.14")
float(10)
str(3.14)
str(True)
int(True)
bool(0)
bool("False")   # deliberately tricky — a non-empty string is truthy REGARDLESS of what it says
# done with exercise two.
# The last one is worth noticing something about, it still returns true becaues a bool value with an empty string is the only one that is seen as a false value, so far as it has a value and the value has a sting that is not empty, it will return True even though ther is False written as the string.
