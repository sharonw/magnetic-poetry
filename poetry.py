"""
Generate a word list for quotes from your favorite movie.

Inspired by the original magnet sets:
http://magneticpoetry.com/category/voices-word-magnets/
"""

import re
SRE_MATCH_TYPE = type(re.match("", ""))

names = set()
quotes = open('mean-girls.txt', 'r')

regex = re.compile("^[A-Za-z.' ]*:")
for line in quotes:
    m = regex.match(line)

    # If we found a match, m is SRE_Match
    # Otherwise, if there's no match, it's NoneType

    if type(m) is SRE_MATCH_TYPE:
        name = m.group()
        names.add(name[:-1])

print names
