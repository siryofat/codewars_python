'''
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
'''

def remove_exclamation_marks(s: str) -> str:
    import re
    return re.sub('!', '', s)

print(remove_exclamation_marks('Hello! world!!!'))