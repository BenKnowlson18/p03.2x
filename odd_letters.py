"""
Problem:

    Amazingly, humans can often read words with most of the
    letters missing from them and still make sense of it.
    To test this, we will be writing a function that removes
    every other letter from a piece of text, starting with
    the second character.

    For example: 'harmonise' -> 'hrose'

    Maybe making sense of it isn't so easy after all!

    Create the function 'reduce'

Tests:

    >>> reduce('harmonise')
    hroie
    >>> reduce('diplodocus')
    dpoou
    >>> reduce('tyrannosaurus')
    trnoars

"""

# This code tests your solution. Don't edit it.
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code:
def reduce(text):

    length = len(text)
    newword = ""

    for n in range(length):

        if n % 2 == 0:
            newword = newword + text[n]

    print(newword)
