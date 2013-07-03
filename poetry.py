"""
Generate a word list for quotes from your favorite movie.

Inspired by the original magnet sets:
http://magneticpoetry.com/category/voices-word-magnets/
"""

word_count = dict()
prepositions = open('prepositions.txt', 'r')

for word in prepositions:
    word_count[word.strip()] = 0

names = set()
quotes = open('mean-girls.txt', 'r')

for line in quotes:
    colon = line.find(':')

    if colon != -1:
        names.add(line[:colon])

        dialogue = line[colon+1:].strip().split()
        print dialogue

print '\n\nCharacter names:\n'
print names

print '\n\nOccurrences of prepositions:\n'
print word_count
