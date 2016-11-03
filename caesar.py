"""
Problem:

    Julius Caesar is credited with inventing one of the first ways
    of encrypting messages for transmission. A Caesar cipher works
    by replacing each of the characters in a piece of text with the
    character a certain number of spaces along in the alphabet.

    For example, if we moved 'APE' 3 along it would become 'DSH'.
    
    Moving past 'Z' should take us back to 'A'.

    The function 'encode' takes a piece of text and should move
    it along the alphabet n spaces.

    The function 'decode' should do the opposite.

    All text will be given in uppercase. No punctuation will be
    included, other than spaces - these should not be encoded.

Tests:

    >>> encode("APE", 3)
    DSH
    >>> encode("HELLO WORLD", 12)
    TQXXA IADXP
    >>> encode("JULIUS CAESAR", 9)
    SDURDB LJNBJA
    >>> decode("DSH", 3)
    APE
    >>> decode("SDURB LJNBJA", 9)
    JULIS CAESAR
    >>> decode("TQXXA IADXP", 12)
    HELLO WORLD

"""

# This code tests your solution. Don't edit it.
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code:
def encode(text, n):

    length = len(text)
    newword = ""
    newletter = ""

    for i in range(length):
        if text[i] == " ":
            newword = newword + text[i]

        elif text[i] != " ":
            newletter = ord(text[i]) + n
            newword = newword + chr(newletter)

    print(newword)



def decode(text, n):

    length = len(text)
    newword = ""
    newletter = ""

    for i in range(length):
        if text[i] == " ":
            newword = newword + text[i]

        elif text[i] != " ":
            newletter = ord(text[i]) - n
            newword = newword + chr(newletter)

    print(newword)
