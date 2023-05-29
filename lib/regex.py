import re

my_pattern = r"(It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)"
my_regex = re.compile(my_pattern)

# Test strings
strings = [
    "It's such a lovely day today.",
    "Some weather we're having today, huh?",
    "Maybe today's just not my day.",
    "This is a different string."
]

# Find matches
matches = [string for string in strings if my_regex.search(string)]

# Assert matches
assert matches == [
    "It's such a lovely day today.",
    "Some weather we're having today, huh?",
    "Maybe today's just not my day."
]