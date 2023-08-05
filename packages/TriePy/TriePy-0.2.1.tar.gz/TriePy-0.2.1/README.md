TriePy
===========

A simple trie implementation in Python

This implementation utilizes a dictionary as its backing
data structure. Essentially, it is creating nested dictionaries.


Example
----------
    >>> from trie import TriePy
    >>> t = TriePy()
    >>> t.add_word("dog")
    >>> t.add_word("doggy")
    >>> t.add_word("dogs")
    >>> t.contains_word("dog")
    True
    >>> t.contains_word("dogg")
    False
    >>> t.root
    {'d': {'o': {'g': {'\0': {'word': 'dog'}, 's': {'\0': {'word': 'dogs'}}, 'g': {'y': {'\0': {'word': 'doggy'}}}}}}}


Unit Testing
----------
nose is used for unit testing and simple unit tests
can be run with the following in the source trie directory:
    `nosetests`


Installation
----------
You can install this as usual with `setup.py`. 
    `python setup.py install`

You can also install this via pip.
    `pip install TriePy`

The usual "use virtualenv to test first" warnings apply.
