
from string import ascii_lowercase

def swap_case(s):
    new = ""
    for letter in s:
        if letter in ascii_lowercase:
            new += letter.upper()
        else:
            new += letter.lower()
    return new

