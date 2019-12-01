import re

def fraction(phrase: str) -> str:
    "Return first fraction or blank"
    find = '[+-]\d\d*/\d\d*'
    match = re.search(find, phrase)
    if match:
        return match
    else:
        return ""

print(fraction("This is +1 /3 true and -2/ 3 false"))