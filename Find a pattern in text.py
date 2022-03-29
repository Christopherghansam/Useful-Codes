import re


def text_match(text):
    patterns = '^[a-zA-Z0-9_]*$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print("text#1: " + text_match("The quick brown fox jumps over the lazy dog."))
print("text#2: " + text_match("Python_Exercises_1"))
