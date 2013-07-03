"""
Generate a word list for quotes from your favorite movie.

Inspired by the original magnet sets:
http://magneticpoetry.com/category/voices-word-magnets/
"""

def build_dialogue_frequency(tokens):
    count = dict()
    for word in tokens:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

def update_max_counts(line_count, proposition_count):
    for word in line_count:
        if word in proposition_count and proposition_count[word] < line_count[word]:
            proposition_count[word] = line_count[word]
    return proposition_count

def print_word_count(word_count):
    for word in word_count:
        if word_count[word] > 0:
            print "%d  %s" % (word_count[word], word)

prepositions = open('prepositions.txt', 'r')
quotes = open('mean-girls.txt', 'r')

word_count = dict()
names = set()

for word in prepositions:
    word_count[word.strip()] = 0

for line in quotes:
    colon = line.find(':')

    if colon != -1:
        names.add(line[:colon])

        dialogue = line[colon+1:].strip().split()
        token_count = build_dialogue_frequency(dialogue)
        word_count = update_max_counts(token_count, word_count)

print '\n\nCharacter names:\n'
print names

print '\n\nOccurrences of prepositions:\n'
print_word_count(word_count)
