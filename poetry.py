"""
Generate a word list for quotes from your favorite movie.

Inspired by the original magnet sets:
http://magneticpoetry.com/category/voices-word-magnets/
"""

import re

names = set()
quotes = open('mean-girls.txt', 'r')

regex = re.compile("^[A-Za-z. ]*")
for line in quotes:
    m = regex.match(line)
    names.add(m.group())

print names
