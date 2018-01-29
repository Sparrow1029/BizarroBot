"""This module contains the dictionary thesarus of BIZARRO TRUMP!!!"""

class trumpsaurus():
    """Easier to import a class I guess. I'm new to this stuff."""
    x = {
        'good': 'bad',
        'bigly': 'quietly',
        'big': 'small',
        'huge': 'tiny',
        'america': 'russia',
        'usa': 'my kingdom',
        'u.s.a.': 'my kingdom',
        'mexico': 'TACO WORLD',
        'sad': 'happy',
        'better': 'worse',
        'innocent': 'guilty',
        'mourn': 'celebrate',
        'resolve': 'obfuscate',
        'never': 'always',
        'safety': 'danger',
        'many': 'few',
        'security': 'danger',
        'might': 'weakness',
        'evil': 'benificent',
        'courage': 'cowardice',
        'i': 'King Trump',
        'we': 'I',
        'you': 'me',
        'us': 'myself',
        'interested': 'bored',
        'brave': 'cowardly',
        'right': 'wrong',
        'long': 'short',
        'wonderful': 'terrible',
        'black': 'white'
    }

    y = {v: k for k, v in x.items()}

    antonyms = {**x, **y}

# print(trumpsaurus().antonyms)
